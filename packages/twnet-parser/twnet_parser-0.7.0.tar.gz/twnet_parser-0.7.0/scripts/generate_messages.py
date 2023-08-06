#!/usr/bin/env python3

import os
import json

from typing import \
    TypedDict, Literal, Optional, Dict, Union, TextIO, Annotated

KINDCONLESS = Literal[ \
            'packed_addresses', \
            'be_uint16', \
            'uint8']

KIND = Literal[ \
            'int32', \
            'tick', \
            'string', \
            'raw', \
            'sha256', \
            'data', \
            'rest', \
            'enum', \
            'boolean', \
            'tune_param', \
            'snapshot_object', \
            'array', \
            'flags', \
            'optional']

class GameEnumValueJson(TypedDict):
    value: int
    name: list[str]

class GameEnumJson(TypedDict):
    name: list[str]
    values: list[GameEnumValueJson]

class ConstantJson(TypedDict):
    name: list[str]
    type: str
    value: int

class InnerNetMessageMemberTypeJson(TypedDict):
    kind: KIND
    disallow_cc: bool

class ArrayMemberTypeJson(TypedDict):
    kind: KIND
    # strings
    disallow_cc: bool

    # array in array only for de client info
    # type forward declaration or self reference is not supported
    # so hack it with a string
    member_type: 'ArrayMemberTypeJson'
    count: int

class NetConnlessMemberTypeJson(TypedDict):
    kind: KINDCONLESS

class NetMessageMemberTypeJson(TypedDict):
    kind: KIND
    inner: InnerNetMessageMemberTypeJson

    # enums
    enum: list[str]

    # strings
    disallow_cc: bool

    # arrays
    count: int
    member_type: ArrayMemberTypeJson

    # data
    size: Literal['specified_before']

class NetMessageMemberJson(TypedDict):
    name: list[str]
    type: NetMessageMemberTypeJson

class NetMessageJson(TypedDict):
    id: int
    name: list[str]
    members: list[NetMessageMemberJson]
    attributes: list[Literal['msg_encoding']]

class NetConnlessJson(TypedDict):
    id: Annotated[list[int], 8]
    name: list[str]
    members: list[NetMessageMemberJson]

class SpecJson(TypedDict):
    constants: list[ConstantJson]
    game_enumerations: list[GameEnumJson]
    game_messages: list[NetMessageJson]
    system_messages: list[NetMessageJson]
    connless_messages: list[NetConnlessJson]
    snapshot_objects: list[NetMessageJson]

def fix_name_conflict(name: str) -> str:
    # https://peps.python.org/pep-0008/#descriptive-naming-styles
    if name in ('pass', 'self'):
        return f'{name}_'
    return name

def name_to_camel(name_list: list[str]) -> str:
    name = ''.join([part.capitalize() for part in name_list])
    return fix_name_conflict(name)

def name_to_snake(name_list: list[str]) -> str:
    name = '_'.join(name_list)
    return fix_name_conflict(name)

def gen_unpack_members_connless7(msg: NetConnlessJson) -> str:
    res: str = ''
    for member in msg['members']:
        unpacker = 'int()'
        name = name_to_snake(member["name"])
        if member['type']['kind'] == 'be_uint16':
            unpacker = 'be_uint16()'
        elif member['type']['kind'] == 'uint8':
            unpacker = 'uint8()'
        elif member['type']['kind'] == 'int32':
            unpacker = 'int()'
        elif member['type']['kind'] == 'int32_string':
            res += f'        self.{name} = int(unpacker.get_str())\n'
            continue
        elif member['type']['kind'] == 'string':
            if member['type']['disallow_cc']:
                unpacker = 'str(SANITIZE_CC)'
            else:
                unpacker = 'str()'
        elif member['type']['kind'] == 'serverinfo_client': # TODO: serverinfo_client
            unpacker = 'raw()'
        elif member['type']['kind'] == 'packed_addresses':
            unpacker = 'packed_addresses()'
        else:
            raise ValueError(f"Error: unknown type {member['type']}")
        res += f'        self.{name} = unpacker.get_{unpacker}\n'
    return res

def gen_unpack_members(msg: NetMessageJson) -> str:
    res: str = ''
    for member in msg['members']:
        # {'name': ['message'], 'type': {'kind': 'string', 'disallow_cc': False}} 
        unpacker = 'int()'
        if member['type']['kind'] == 'string':
            if member['type']['disallow_cc']:
                unpacker = 'str(SANITIZE_CC)'
            else:
                unpacker = 'str()'
        elif member['type']['kind'] == 'rest':
            unpacker = 'raw()'
        elif member['type']['kind'] == 'sha256':
            unpacker = 'raw(32)'
        elif member['type']['kind'] == 'data':
            if member['type']['size'] == 'specified_before':
                res += '        self.data_size = unpacker.get_int()\n'
                unpacker = 'raw(self.data_size)'
            else:
                raise ValueError(f"Error: unknown data size {member['type']}")
        # {"name": ["mode"], "type": {"kind": "enum", "enum": ["chat"]}},
        elif member['type']['kind'] == 'enum':
            enum_name: str = name_to_camel(member['type']['enum']).upper()
            unpacker = f"int() # enum {enum_name}"
        elif member['type']['kind'] in ('int32', 'tick'):
            unpacker = 'int()'
        elif member['type']['kind'] == 'boolean':
            unpacker = 'int() == 1'
        elif member['type']['kind'] == 'tune_param':
            unpacker = 'int() / 100.0'
        elif member['type']['kind'] == 'snapshot_object':
            # TODO: think about snapshot_object
            unpacker = 'int() # TODO: this is a snapshot object'
        elif member['type']['kind'] == 'array':
            size: int = member['type']['count']
            if size is None:
                print("Error: size is none for the following message")
                print(msg)
                exit(1)
            arr_member: ArrayMemberTypeJson = member['type']['member_type']
            if arr_member['kind'] == 'string':
                if arr_member['disallow_cc']:
                    unpacker = 'str(SANITIZE_CC)'
                else:
                    unpacker = 'str()'
            elif arr_member['kind'] == 'enum':
                # We intentionally do not do anything fancy here
                # no enums for example because it comes with too many
                # disadvantages see the related issue here
                # https://gitlab.com/teeworlds-network/twnet_parser/-/issues/7
                unpacker = 'int()'
            elif arr_member['kind'] == 'boolean':
                unpacker = 'int() == 1'
            elif arr_member['kind'] in ('int32', 'tick'):
                unpacker = 'int()'
            elif arr_member['kind'] == 'array':
                sub_size: int = arr_member['count']
                sub_arr_member = arr_member['member_type']
                unpacker = 'int()'
                if sub_arr_member['kind'] == 'int32':
                    name = name_to_snake(member["name"])
                    res += f'        for i in range(0, {size}):\n'
                    res +=  '            sub: list[int] = []\n'
                    res += f'            for k in range(0, {sub_size}):\n'
                    res += f'                sub[k] = unpacker.get_{unpacker}\n'
                    res += f'            self.{name}[i] = sub\n'
                    continue
                else:
                    raise ValueError(
                            f"Error: unknown sub array member type {member['type']}"
                    )
            else:
                raise ValueError(f"Error: unknown array member type {member['type']}")
            name = name_to_snake(member["name"])
            res += f'        for i in range(0, {size}):\n'
            res += f'            self.{name}[i] = unpacker.get_{unpacker}\n'
            continue
        elif member['type']['kind'] == 'flags': # TODO: think about flags
            unpacker = 'int() # TODO: this is a flag'
        elif member['type']['kind'] == 'optional':
            # TODO: unpacker should not crash on missing optional fields
            #       check how tw code does it and be smart here
            if member['type']['inner']['kind'] == 'string':
                if member['type']['inner']['disallow_cc']:
                    unpacker = 'str(SANITIZE_CC)'
                    unpacker += ' # TODO: optionals'
                else:
                    unpacker = 'str() # TODO: optionals'
            elif member['type']['inner']['kind'] in ('int32', 'tick'):
                unpacker = 'int() # TODO: optionals'
        else:
            raise ValueError(f"Error: unknown type {member['type']}")
        name = name_to_snake(member["name"])
        res += f'        self.{name} = unpacker.get_{unpacker}\n'
    return res

def pack_field(member: NetMessageMemberJson) -> str:
    name: str = name_to_snake(member["name"])
    field: str = f'self.{name}'
    packer = 'int'
    if member['type']['kind'] == 'string':
        packer = 'str'
    elif member['type']['kind'] in ('sha256', 'rest'):
        return f'self.{name}'
    elif member['type']['kind'] == 'data':
        if member['type']['size'] == 'specified_before':
            return f'pack_int(self.data_size) + \\\n' \
                f'            self.{name}'
        else:
            raise ValueError(f"Error: unknown data size {member['type']}")
    # {"name": ["mode"], "type": {"kind": "enum", "enum": ["chat"]}},
    elif member['type']['kind'] == 'enum':
        packer = 'int'
    elif member['type']['kind'] in ('int32', 'tick'):
        packer = 'int'
    elif member['type']['kind'] == 'boolean':
        packer = 'int'
    elif member['type']['kind'] == 'tune_param':
        packer = 'int'
        field = f'int({field} * 100.0)'
    elif member['type']['kind'] == 'snapshot_object':
        # TODO: think about snapshot_object
        packer = 'int'
    elif member['type']['kind'] == 'array':
        arr_member: ArrayMemberTypeJson = member['type']['member_type']
        if arr_member['kind'] == 'string':
           packer = 'str'
        elif arr_member['kind'] == 'enum':
           packer = 'int'
        elif arr_member['kind'] == 'boolean':
           packer = 'int'
        elif arr_member['kind'] in ('int32', 'tick'):
           packer = 'int'
        elif arr_member['kind'] == 'array':
            sub_arr_member = arr_member['member_type']
            if sub_arr_member['kind'] == 'int32':
                return f"b''.join([b''.join([pack_{packer}(x) for x in sub]) for sub in {field}])"
            else:
               raise ValueError(f"Error: unknown sub array member type {member['type']}")
        else:
           raise ValueError(f"Error: unknown array member type {member['type']}")
        return f"b''.join([pack_{packer}(x) for x in {field}])"
    elif member['type']['kind'] == 'flags': # TODO: think about flags
        packer = 'int'
    elif member['type']['kind'] == 'optional':
        packer = 'int'
        # TODO: unpacker should allow not packing optional fields
        #       check how tw code does it and be smart here
        if member['type']['inner']['kind'] == 'string':
            packer = 'str'
        elif member['type']['inner']['kind'] in ('int32', 'tick'):
            packer = 'int'
    else:
        raise ValueError(f"Error: unknown type {member['type']}")
    return f'pack_{packer}({field})'

def gen_pack_return(msg: NetMessageJson) -> str:
    members: list[NetMessageMemberJson] = msg['members']
    if len(members) == 0:
        return "        return b''"
    if len(members) == 1:
        return f'        return {pack_field(members[0])}'
    mem_strs: list[str] = [
            f'            {pack_field(member)}' for member in members[1:]]
    return f"        return {pack_field(members[0])} + \\\n" + \
            ' + \\\n'.join(mem_strs)

def pack_field_connless7(member: NetMessageMemberJson) -> str:
    name: str = name_to_snake(member["name"])
    field: str = f'self.{name}'
    packer = 'int'
    if member['type']['kind'] == 'packed_addresses':
        packer = 'packed_addresses'
    elif member['type']['kind'] == 'be_uint16':
        packer = 'be_uint16'
    elif member['type']['kind'] == 'uint8':
        packer = 'uint8'
    elif member['type']['kind'] == 'string':
        packer = 'str'
    elif member['type']['kind'] == 'int32':
        packer = 'int'
    elif member['type']['kind'] == 'int32_string':
        return f'pack_str(str({field}))'
    elif member['type']['kind'] == 'serverinfo_client': # TODO: serverinfo_client
        return f'self.{name}'
    else:
        raise ValueError(f"Error: unknown type {member['type']}")
    return f'pack_{packer}({field})'

def gen_pack_return_connless7(msg: NetConnlessJson) -> str:
    members: list[NetMessageMemberJson] = msg['members']
    if len(members) == 0:
        return "        return b''"
    if len(members) == 1:
        return f'        return {pack_field_connless7(members[0])}'
    mem_strs: list[str] = [
            f'            {pack_field_connless7(member)}' for member in members[1:]]
    return f"        return {pack_field_connless7(members[0])} + \\\n" + \
            ' + \\\n'.join(mem_strs)

def get_default(field_path: str) -> Optional[str]:
    """
    field_path has the following format:

        game.msg_name.field_name

    example:

        game.sv_tune_params.ground_control_speed
    """
    # COULDDO: make this faster
    #          but then who cares about
    #          code gen speed
    def_file: str = './data/messages7_defaults.json'
    if not os.path.exists(def_file):
        print(f"Failed to open defaults file '{def_file}'")
        exit(1)
    with open(def_file) as def_io:
        def_json: Dict[str, Union[int, float, bool, str]] = json.load(def_io)
        if field_path not in def_json:
            return None
        default = def_json[field_path]
        # also covers bool cuz python drunk
        # but this is actually exactly what we want
        if isinstance(default, int):
            return str(default)
        elif isinstance(default, float):
            return str(default)
        elif isinstance(default, str):
            return f"'{default}'"
        else:
            print(f"Error: invalid default type for field {field_path}")
            print(f"        please check {def_file} for errors")
            exit(1)

class CodeGenerator():
    def __init__(self, protocol_version: str) -> None:
        self.protocol_version = protocol_version
        self.game_enums: list[GameEnumJson] = []

    def get_dependencies_connless(self, msg: NetConnlessJson) -> str:
        packer_deps: list[str] = []
        typing_deps: list[str] = ['Literal']
        res: str = ''
        for member in msg['members']:
            if member['type']['kind'] == 'packed_addresses':
                packer_deps.append('pack_packed_addresses')
                res += 'from twnet_parser.master_server import MastersrvAddr\n'
            elif member['type']['kind'] == 'uint8':
                packer_deps.append('pack_uint8')
            elif member['type']['kind'] == 'be_uint16':
                packer_deps.append('pack_be_uint16')
            elif member['type']['kind'] == 'int32':
                packer_deps.append('pack_int')
            elif member['type']['kind'] == 'int32_string':
                packer_deps.append('pack_str')
            elif member['type']['kind'] == 'serverinfo_client': # TODO: serverinfo_client
                pass # use pack raw
            elif member['type']['kind'] == 'string':
                packer_deps.append('pack_str')
                if member['type']['disallow_cc']:
                    packer_deps.append('SANITIZE_CC')
            else:
                raise ValueError(f"Error: unknown type {member['type']}")
        if len(packer_deps) > 0:
            res += 'from twnet_parser.packer import ' + \
                ', '.join(sorted(set(packer_deps))) + '\n'
        if len(typing_deps) > 0:
            res += 'from typing import ' + \
                ', '.join(sorted(set(typing_deps))) + '\n'
        return res

    def get_dependencies(
            self,
            msg: NetMessageJson,
            typing_dep: Optional[str] = 'Literal'
    ) -> str:
        packer_deps: list[str] = []
        typing_deps: list[str] = []
        if typing_dep:
            typing_deps.append(typing_dep)
        need_enums: bool = False
        for member in msg['members']:
            if member['type']['kind'] == 'string':
                packer_deps.append('pack_str')
                if member['type']['disallow_cc']:
                    packer_deps.append('SANITIZE_CC')
            elif member['type']['kind'] == 'rest':
                pass
            elif member['type']['kind'] == 'sha256':
                typing_deps.append('Annotated')
            elif member['type']['kind'] == 'data':
                if member['type']['size'] == 'specified_before':
                    typing_deps.append('Optional')
                else:
                    raise ValueError(f"Error: unknown data size {member['type']}")
            # {"name": ["mode"], "type": {"kind": "enum", "enum": ["chat"]}},
            elif member['type']['kind'] == 'enum':
                need_enums = True
                packer_deps.append('pack_int')
            elif member['type']['kind'] in ('int32', 'tick'):
                packer_deps.append('pack_int')
            elif member['type']['kind'] == 'boolean':
                packer_deps.append('pack_int')
            elif member['type']['kind'] == 'tune_param':
                packer_deps.append('pack_int')
            elif member['type']['kind'] == 'snapshot_object':
                # TODO: think about snapshot_object
                packer_deps.append('pack_int')
            elif member['type']['kind'] == 'array':
                packer_deps.append('pack_int')
                typing_deps.append('Annotated')
                arr_member: ArrayMemberTypeJson = member['type']['member_type']
                if arr_member['kind'] == 'string':
                    packer_deps.append('pack_str')
                    if arr_member['disallow_cc']:
                        packer_deps.append('SANITIZE_CC')
                elif arr_member['kind'] == 'enum':
                    need_enums = True
                    packer_deps.append('pack_int')
                elif arr_member['kind'] == 'boolean':
                    packer_deps.append('pack_int')
                elif arr_member['kind'] in ('int32', 'tick'):
                    packer_deps.append('pack_int')
                elif arr_member['kind'] == 'array':
                    if arr_member['member_type']['kind'] == 'int32':
                        packer_deps.append('pack_int')
                    else:
                        raise ValueError(
                                f"Error: unknown sub array member type {member['type']}"
                        )
                else:
                    raise ValueError(f"Error: unknown array member type {member['type']}")
            elif member['type']['kind'] == 'flags': # TODO: think about flags
                packer_deps.append('pack_int')
            elif member['type']['kind'] == 'optional':
                if member['type']['inner']['kind'] == 'string':
                    packer_deps.append('pack_str')
                    if member['type']['inner']['disallow_cc']:
                        packer_deps.append('SANITIZE_CC')
                elif member['type']['inner']['kind'] in ('int32', 'tick'):
                    packer_deps.append('pack_int')
            else:
                raise ValueError(f"Error: unknown type {member['type']}")
        res: str = ''
        if len(packer_deps) > 0:
            res += 'from twnet_parser.packer import ' + \
                ', '.join(sorted(set(packer_deps))) + '\n'
        if len(typing_deps) > 0:
            res += 'from typing import ' + \
                ', '.join(sorted(set(typing_deps))) + '\n'
        if need_enums:
            res += f'import twnet_parser.enum{self.protocol_version} as enum{self.protocol_version}\n'
        return res

    def gen_match_file(
            self,
            msg_type: Literal['system', 'game'],
            messages: list[NetMessageJson]
    ):
        match_code: str = f"""# generated by scripts/generate_messages.py
from typing import Optional

import twnet_parser.msg{self.protocol_version}
from twnet_parser.net_message import NetMessage

"""

        msg: NetMessageJson
        for msg in messages:
            name_snake = name_to_snake(msg['name'])
            match_code += f"import twnet_parser.messages{self.protocol_version}.{msg_type}" \
                    f".{name_snake}" \
                    " as \\\n" \
                    f"       {msg_type}{self.protocol_version}_{name_snake}\n"

        match_code += f"""
def match_{msg_type}{self.protocol_version}(msg_id: int, data: bytes) -> NetMessage:
    msg: Optional[NetMessage] = None
"""

        if_ = 'if'
        for msg in messages:
            name_snake = name_to_snake(msg['name'])
            name_camel = name_to_camel(msg['name'])
            match_code += f"""
    {if_} msg_id == twnet_parser.msg{self.protocol_version}.{name_snake.upper()}:
        msg = {msg_type}{self.protocol_version}_{name_snake}.Msg{name_camel}()"""
            if_ = 'elif'

        match_code += '\n\n    if msg is None:\n'
        match_code += '        '
        match_code += 'raise ValueError('
        match_code += 'f"Error: unknown ' \
                + msg_type + \
                ' message id={msg_id} data={data[0]}")\n'
        match_code += '\n'
        match_code += '    msg.unpack(data)\n'
        match_code += '    return msg\n'

        dirname = os.path.dirname(__file__)
        file_path= os.path.join(
                dirname,
                f'../twnet_parser/msg_matcher/{msg_type}{self.protocol_version}.py')
        # if os.path.exists(file_path):
        #     print(f"Warning: file already exists! {file_path}")
        #     return
        with open(file_path, 'w') as out_file:
            print(f"Generating {file_path} ...")
            out_file.write(match_code)

    def gen_match_file_connless(
            self,
            messages: list[NetConnlessJson]
    ):
        match_code: str = f"""# generated by scripts/generate_messages.py
from typing import Optional

import twnet_parser.msg{self.protocol_version}
from twnet_parser.connless_message import ConnlessMessage

"""

        msg: NetConnlessJson
        for msg in messages:
            name_snake = name_to_snake(msg['name'])
            match_code += f"import twnet_parser.messages{self.protocol_version}.connless" \
                    f".{name_snake}" \
                    " as \\\n" \
                    f"       connless_{name_snake}\n"

        match_code += f"""
def match_connless{self.protocol_version}(msg_id: bytes, data: bytes) -> ConnlessMessage:
    msg: Optional[ConnlessMessage] = None
"""

        if_ = 'if'
        for msg in messages:
            name_snake = name_to_snake(msg['name'])
            name_camel = name_to_camel(msg['name'])
            match_code += \
    f"""
    {if_} msg_id == twnet_parser.msg{self.protocol_version}.CONNLESS_{name_snake.upper()}:
        msg = connless_{name_snake}.Msg{name_camel}()"""
            if_ = 'elif'

        match_code += '\n\n    if msg is None:\n'
        match_code += '        '
        match_code += 'raise ValueError(\n'
        match_code += '            '
        match_code += 'f"Error: unknown conless ' \
                ' message id={msg_id!r} data={data[0]}"\n'
        match_code += '        )\n'
        match_code += '\n'
        match_code += '    msg.unpack(data)\n'
        match_code += '    return msg\n'

        dirname = os.path.dirname(__file__)
        file_path= os.path.join(
                dirname,
                f'../twnet_parser/msg_matcher/connless{self.protocol_version}.py')
        with open(file_path, 'w') as out_file:
            print(f"Generating {file_path} ...")
            out_file.write(match_code)

    def gen_init_member_header_def(
            self,
            member: NetMessageMemberJson,
            name_snake: str,
            message_type: Literal['game', 'system', 'connless', 'snap']
    ) -> list[str]:
        """
        get_init_member_header_def

        given a member field it returns an array of strings
        that represent the python code for the content in the
        init method parameter list

            def __init__(self, [THIS IS GENERATED]) -> None:

        it might return two fields for members like data
        that also introduce a size field

        the returned assignements do not include indentation
        """
        args: list[str] = []
        # {
        #   'name': ['message'],
        #   'type': {
        #     'kind': 'string',
        #     'disallow_cc': False
        #   }
        # }
        ftype = 'int'
        default = '-1'
        if member['type']['kind'] == 'string':
            ftype = 'str'
            default = "'default'"
        elif member['type']['kind'] == 'packed_addresses': # TODO: packed_addreses default value
            ftype = 'list[MastersrvAddr]'
            default = '[]'
        elif member['type']['kind'] == 'serverinfo_client': # TODO: serverinfo_client
            ftype = 'bytes'
            default = "b''"
        elif member['type']['kind'] == 'be_uint16':
            ftype = 'int'
            default = '0'
        elif member['type']['kind'] == 'uint8':
            ftype = 'int'
            default = '0'
        elif member['type']['kind'] == 'rest':
            ftype = 'bytes'
            default = "b'\\x00'"
        elif member['type']['kind'] == 'sha256':
            ftype = 'Annotated[bytes, 32]'
            default = "bytes(32)"
        elif member['type']['kind'] == 'data':
            ftype = 'bytes'
            default = "b'\\x00'"
            if member['type']['size'] == 'specified_before':
                args.append('data_size: Optional[int] = None')
            else:
                raise ValueError(f"Error: unknown data size {member['type']}")
        # {"name": ["mode"], "type": {"kind": "enum", "enum": ["chat"]}},
        elif member['type']['kind'] == 'enum':
            enum_name: str = name_to_camel(member['type']['enum'])
            ftype = 'int'
            default = self.get_default_enum(enum_name)
            default = f"enum{self.protocol_version}.{default}.value"
        elif member['type']['kind'] in ('int32', 'tick', 'int32_string'):
            ftype = 'int'
            default = '0'
        elif member['type']['kind'] == 'boolean':
            ftype = 'bool'
            default = 'False'
        elif member['type']['kind'] == 'tune_param':
            ftype = 'float'
            default = '0.0'
        elif member['type']['kind'] == 'snapshot_object':
            # TODO: think about snapshot_object
            ftype = 'int'
            default = '0'
        elif member['type']['kind'] == 'array':
            size: int = member['type']['count']
            if size is None:
                print("Error: size is none for the following member")
                print(member)
                exit(1)
            arr_member: ArrayMemberTypeJson = member['type']['member_type']
            if arr_member['kind'] == 'string':
                ftype = f'Annotated[list[str], {size}]'
                default = '[' + ', '.join(["''"] * size) + ']'
            elif arr_member['kind'] == 'boolean':
                ftype = f'Annotated[list[bool], {size}]'
                default = '[' + ', '.join(["False"] * size) + ']'
            elif arr_member['kind'] in ('int32', 'tick', 'enum'):
                ftype = f'Annotated[list[int], {size}]'
                default = '[' + ', '.join(["0"] * size) + ']'
            elif arr_member['kind'] == 'array': # snap de client info has an array of int32 arrays as field
                # should probably do some kind of recursion here
                # but it breaks my brain
                sub_size: int = arr_member['count']
                if sub_size is None:
                    print("Error: size is none for the following sub member")
                    print(arr_member)
                    exit(1)
                sub_arr_member: ArrayMemberTypeJson = arr_member['member_type']
                if sub_arr_member['kind'] == 'int32':
                    ftype = f'Annotated[list[list[int]], ({size},{sub_size})]'
                    inner_default = '[' + ', '.join(["0"] * sub_size) + ']'
                    default = '[' + ',\n                 '.join([inner_default] * size) + ']'
                else:
                    raise ValueError( \
                        f"Error: msg {name_to_snake(member['name'])} " \
                        f"has unknown array sub member type {member['type']}")
            else:
                raise ValueError( \
                    f"Error: msg {name_to_snake(member['name'])} " \
                    f"has unknown array member type {member['type']}")
            # Initializing lists with defaults
            # And type annotation can get quite long
            # So split it in two lines
            default = f'\\\n                {default}'
        elif member['type']['kind'] == 'flags': # TODO: think about flags
            ftype = 'int'
            default = '0'
        elif member['type']['kind'] == 'optional':
            if member['type']['inner']['kind'] == 'string':
                ftype = 'str'
                default = "''"
            elif member['type']['inner']['kind'] in ('int32', 'tick'):
                ftype = 'int'
                default = '0'
            else:
                raise \
                    ValueError( \
                    f"Error: unknown optional type {member['type']}")
        else:
            raise ValueError(f"Error: unknown type {member['type']}")
        name = name_to_snake(member["name"])
        manual_default = get_default(f"{message_type}.{name_snake}.{name}")
        if manual_default:
            default = manual_default
        args.append(f'{name}: {ftype} = {default}')
        return args

    def write_init_method_header_connless(
            self,
            out_file: TextIO,
            msg: NetConnlessJson,
            name_snake: str
    ) -> None:
        comma: str = ''
        if len(msg['members']) > 0:
            comma = ',\n'
        out_file.write( \
            '    def __init__(\n' \
            f'            self{comma}')
        args: list[str] = []
        for member in msg['members']:
            mem_defs: list[str] = self.gen_init_member_header_def(member, name_snake, 'connless')
            for mem_def in mem_defs:
                args.append(f'            {mem_def}')
        out_file.write(',\n'.join(args) + '\n')
        out_file.write('    ) -> None:\n')

    def write_init_method_header(
            self,
            out_file: TextIO,
            msg: NetMessageJson,
            game: Literal['system', 'game'],
            name_snake: str
    ) -> None:
        comma: str = ''
        if len(msg['members']) > 0:
            comma = ',\n'
        out_file.write( \
            '    def __init__(\n' \
            '            self,\n' \
            f'            chunk_header: ChunkHeader = ChunkHeader(){comma}')
        args: list[str] = []
        for member in msg['members']:
            mem_defs: list[str] = self.gen_init_member_header_def(member, name_snake, game)
            for mem_def in mem_defs:
                args.append(f'            {mem_def}')
        out_file.write(',\n'.join(args) + '\n')
        out_file.write('    ) -> None:\n')

    def generate_snap_obj7(self, obj: NetMessageJson) -> None:
        name_snake = name_to_snake(obj['name'])
        name_camel = name_to_camel(obj['name'])
        dirname = os.path.dirname(__file__)
        file_path= os.path.join(
                dirname,
                f'../twnet_parser/snap/0{self.protocol_version}/',
                f'{name_snake}.py')
        with open(file_path, 'w') as out_file:
            print(f"Generating {file_path} ...")
            out_file.write('# generated by scripts/generate_messages.py\n')
            out_file.write('\n')
            out_file.write('from twnet_parser.pretty_print import PrettyPrint\n')
            if len(obj['members']) > 0:
                out_file.write('from twnet_parser.packer import Unpacker\n')
            out_file.write(self.get_dependencies(obj, None))
            out_file.write('\n')
            out_file.write(f'class Obj{name_camel}(PrettyPrint):\n')
            comma: str = ''
            if len(obj['members']) > 0:
                comma = ',\n'
            out_file.write( \
                '    def __init__(\n' \
                f'            self{comma}')
            args: list[str] = []
            for member in obj['members']:
                mem_defs: list[str] = self.gen_init_member_header_def(member, name_snake, 'snap')
                for mem_def in mem_defs:
                    args.append(f'            {mem_def}')
            out_file.write(',\n'.join(args) + '\n')
            out_file.write('    ) -> None:\n')
            out_file.write(f"        self.item_name: str = 'connless.{name_snake}'\n")
            out_file.write(f"        self.type_id: int = {obj['id']}\n")
            out_file.write( "        self.id: int = 0\n")
            out_file.write('\n')
            self.generate_field_assignments_in_initialize(obj, out_file)
            out_file.write('\n')
            out_file.write('    # first byte of data\n')
            out_file.write('    # has to be the first byte of the message payload\n')
            out_file.write('    # NOT the chunk header and NOT the message id\n')
            out_file.write('    def unpack(self, data: bytes) -> bool:\n')
            if len(obj['members']) > 0:
                out_file.write('        unpacker = Unpacker(data)\n')
            out_file.write(gen_unpack_members(obj))
            out_file.write('        return True\n')
            out_file.write('\n')
            out_file.write('    def pack(self) -> bytes:\n')
            out_file.write(gen_pack_return(obj))

    def generate_msg_connless(
            self,
            msg: NetConnlessJson
    ) -> None:
        name_snake = name_to_snake(msg['name'])
        name_camel = name_to_camel(msg['name'])
        dirname = os.path.dirname(__file__)
        file_path= os.path.join(
                dirname,
                f'../twnet_parser/messages{self.protocol_version}/connless/',
                f'{name_snake}.py')
        with open(file_path, 'w') as out_file:
            print(f"Generating {file_path} ...")
            out_file.write('# generated by scripts/generate_messages.py\n')
            out_file.write('\n')
            out_file.write('from twnet_parser.pretty_print import PrettyPrint\n')
            if len(msg['members']) > 0:
                out_file.write('from twnet_parser.packer import Unpacker\n')
            out_file.write(self.get_dependencies_connless(msg))
            out_file.write('\n')
            out_file.write(f'class Msg{name_camel}(PrettyPrint):\n')
            self.write_init_method_header_connless(out_file, msg, name_snake)
            out_file.write(f"        self.message_type: Literal['connless'] = 'connless'\n")
            out_file.write(f"        self.message_name: str = 'connless.{name_snake}'\n")
            out_file.write(f"        self.message_id: list[int] = {msg['id']}\n")
            out_file.write('\n')
            for member in msg['members']:
                ftype = 'int'
                if member['type']['kind'] == 'packed_addresses': # TODO: packed_addreses default value
                    ftype = 'list[MastersrvAddr]'
                elif member['type']['kind'] == 'be_uint16': # TODO: be_uint16
                    ftype = 'int'
                elif member['type']['kind'] == 'uint8': # TODO: uint8
                    ftype = 'int'
                elif member['type']['kind'] in ('int32', 'int32_string'):
                    ftype = 'int'
                elif member['type']['kind'] == 'string':
                    ftype = 'str'
                elif member['type']['kind'] == 'serverinfo_client': # TODO: serverinfo_client
                    ftype = 'bytes'
                else:
                    raise ValueError(f"Error: unknown connless type {member['type']}")
                name = name_to_snake(member["name"])
                if ftype != '':
                    ftype = f': {ftype}'
                if member['type']['kind'] == 'enum':
                    out_file.write(f"        self.{name}{ftype} = {name}\n")
                else:
                    out_file.write(f"        self.{name}{ftype} = {name}\n")
            out_file.write('\n')
            out_file.write('    # first byte of data\n')
            out_file.write('    # has to be the first byte of the message payload\n')
            out_file.write('    # NOT the chunk header and NOT the message id\n')
            out_file.write('    def unpack(self, data: bytes) -> bool:\n')
            if len(msg['members']) > 0:
                out_file.write('        unpacker = Unpacker(data)\n')
            out_file.write(gen_unpack_members_connless7(msg))
            out_file.write('        return True\n')
            out_file.write('\n')
            out_file.write('    def pack(self) -> bytes:\n')
            out_file.write(gen_pack_return_connless7(msg))

    def generate_field_assignments_in_initialize(
            self,
            msg: NetMessageJson,
            out_file
    ) -> None:
        for member in msg['members']:
            # {
            #   'name': ['message'],
            #   'type': {
            #     'kind': 'string',
            #     'disallow_cc': False
            #   }
            # }
            ftype = 'int'
            if member['type']['kind'] == 'string':
                ftype = 'str'
            elif member['type']['kind'] == 'rest':
                ftype = 'bytes'
            elif member['type']['kind'] == 'sha256':
                ftype = 'Annotated[bytes, 32]'
            elif member['type']['kind'] == 'data':
                ftype = 'bytes'
                if member['type']['size'] == 'specified_before':
                    out_file.write("        " \
                        "self.data_size: int =" \
                        " data_size if data_size else len(data)\n")
                else:
                    raise ValueError(f"Error: unknown data size {member['type']}")
            # {"name": ["mode"], "type": {"kind": "enum", "enum": ["chat"]}},
            elif member['type']['kind'] == 'enum':
                ftype = 'int'
            elif member['type']['kind'] in ('int32', 'tick'):
                ftype = 'int'
            elif member['type']['kind'] == 'boolean':
                ftype = 'bool'
            elif member['type']['kind'] == 'tune_param':
                ftype = 'float'
            elif member['type']['kind'] == 'snapshot_object':
                # TODO: think about snapshot_object
                ftype = 'int'
            elif member['type']['kind'] == 'array':
                # Array type annotations are so annoyingly long
                # also there is a planned refactor
                # https://gitlab.com/teeworlds-network/twnet_parser/-/issues/4
                # so inherit type from constructor arguments
                ftype = ''
            elif member['type']['kind'] == 'flags': # TODO: think about flags
                ftype = 'int'
            elif member['type']['kind'] == 'optional':
                if member['type']['inner']['kind'] == 'string':
                    ftype = 'str'
                elif member['type']['inner']['kind'] in ('int32', 'tick'):
                    ftype = 'int'
                else:
                    raise \
                        ValueError( \
                        f"Error: unknown optional type {member['type']}")
            else:
                raise ValueError(f"Error: unknown type {member['type']}")
            name = name_to_snake(member["name"])
            if ftype != '':
                ftype = f': {ftype}'
            if member['type']['kind'] == 'enum':
                out_file.write(f"        self.{name}{ftype} = {name}\n")
            else:
                out_file.write(f"        self.{name}{ftype} = {name}\n")

    def generate_msg(
            self,
            msg: NetMessageJson,
            game: Literal['system', 'game']
    ) -> None:
        name_snake = name_to_snake(msg['name'])
        name_camel = name_to_camel(msg['name'])
        dirname = os.path.dirname(__file__)
        file_path= os.path.join(
                dirname,
                f'../twnet_parser/messages{self.protocol_version}/{game}/',
                f'{name_snake}.py')
        # if os.path.exists(file_path):
        #     print(f"Warning: file already exists! {file_path}")
        #     return
        with open(file_path, 'w') as out_file:
            print(f"Generating {file_path} ...")
            out_file.write('# generated by scripts/generate_messages.py\n')
            out_file.write('\n')
            out_file.write('from twnet_parser.pretty_print import PrettyPrint\n')
            if len(msg['members']) > 0:
                out_file.write('from twnet_parser.packer import Unpacker\n')
            out_file.write('from twnet_parser.chunk_header import ChunkHeader\n')
            out_file.write(self.get_dependencies(msg))
            out_file.write('\n')
            out_file.write(f'class Msg{name_camel}(PrettyPrint):\n')
            self.write_init_method_header(out_file, msg, game, name_snake)
            out_file.write(f"        self.message_type: Literal['system', 'game'] = '{game}'\n")
            out_file.write(f"        self.message_name: str = '{name_snake}'\n")
            sys: str = 'True' if game == 'system' else 'False'
            out_file.write(f"        self.system_message: bool = {sys}\n")
            out_file.write(f"        self.message_id: int = {msg['id']}\n")
            out_file.write("        self.header: ChunkHeader = chunk_header\n")
            out_file.write('\n')
            self.generate_field_assignments_in_initialize(msg, out_file)
            out_file.write('\n')
            out_file.write('    # first byte of data\n')
            out_file.write('    # has to be the first byte of the message payload\n')
            out_file.write('    # NOT the chunk header and NOT the message id\n')
            out_file.write('    def unpack(self, data: bytes) -> bool:\n')
            if len(msg['members']) > 0:
                out_file.write('        unpacker = Unpacker(data)\n')
            out_file.write(gen_unpack_members(msg))
            out_file.write('        return True\n')
            out_file.write('\n')
            out_file.write('    def pack(self) -> bytes:\n')
            out_file.write(gen_pack_return(msg))

    def get_default_enum(self, enum_name: str) -> str:
        """
        enum_name has to be camel case

        If for example enum_name 'chat' is given
        it returns 'CHAT_NONE'
        """
        enum: GameEnumJson
        for enum in self.game_enums:
            base: str = name_to_camel(enum['name'])
            if base != enum_name:
                continue
            val: GameEnumValueJson
            for val in enum['values']:
                sub: str = name_to_snake(val['name']).upper()
                return f"{base}.{sub}"
        raise ValueError(f"Enum not found '{enum_name}'")

    def gen_enum_file(self) -> None:
        enum_code: str = 'from enum import Enum\n\n'
        enum: GameEnumJson
        for enum in self.game_enums:
            base: str = name_to_camel(enum['name'])
            enum_code += f'class {base}(Enum):\n'
            val: GameEnumValueJson
            for val in enum['values']:
                sub: str = name_to_snake(val['name']).upper()
                enum_code += \
                    '    ' \
                    f"{sub}: int = {val['value']}\n"
            enum_code += "\n"
        # cut off last doubled newline
        # because we do not split a section anymore
        enum_code = enum_code[:-1]
        dirname = os.path.dirname(__file__)
        file_path= os.path.join(
                dirname,
                f'../twnet_parser/enum{self.protocol_version}.py')
        # if os.path.exists(file_path):
        #     print(f"Warning: file already exists! {file_path}")
        #     return
        with open(file_path, 'w') as out_file:
            print(f"Generating {file_path} ...")
            out_file.write(enum_code)

    def generate(self, spec: str) -> None:
        print(f"generating classes from {spec} ...")
        with open(spec) as spec_io:
            spec_data: SpecJson = json.load(spec_io)
            # for msg in [spec_data['game_messages'][1]]:
            self.game_enums = spec_data['game_enumerations']
            game_messages: list[NetMessageJson] = spec_data['game_messages']
            system_messages: list[NetMessageJson] = spec_data['system_messages']
            connless_messages: list[NetConnlessJson] = spec_data['connless_messages']
            snapshot_objects: list[NetMessageJson] = spec_data['snapshot_objects']
            self.gen_enum_file()
            self.gen_match_file('game', game_messages)
            self.gen_match_file('system', system_messages)
            self.gen_match_file_connless(connless_messages)
            for msg in game_messages:
                self.generate_msg(msg, 'game')
            for msg in system_messages:
                if msg['name'] == ['snap']:
                    continue
                self.generate_msg(msg, 'system')
            for connless_msg in connless_messages:
                self.generate_msg_connless(connless_msg)
            # for obj in snapshot_objects:
            #     self.generate_snap_obj7(obj)

class SpecInfo:
    def __init__(
            self,
            json_path: str,
            version_name: str
    ) -> None:
        self.json_path = json_path
        self.version_name = version_name

def main() -> None:
    dirname = os.path.dirname(__file__)
    spec_infos: list[SpecInfo] = [
            SpecInfo(
                '../../libtw2/gamenet/generate/spec/teeworlds-0.7.5.json',
                '7'
            ),
    ]
    #         SpecInfo(
    #             '../../libtw2/gamenet/generate/spec/teeworlds-0.6.json',
    #             '6'
    #         )
    # ]
    for spec_info in spec_infos:
        spec_file = os.path.join(
                dirname,
                spec_info.json_path)
        if os.path.exists(spec_file):
            generator = CodeGenerator(spec_info.version_name)
            generator.generate(spec_file)
        else:
            print(f"Error: file not found {spec_file}")
            print("        try running these commands")
            print("")
            print("        git clone git@github.com:heinrich5991/libtw2 ..")

if __name__ == '__main__':
    main()

