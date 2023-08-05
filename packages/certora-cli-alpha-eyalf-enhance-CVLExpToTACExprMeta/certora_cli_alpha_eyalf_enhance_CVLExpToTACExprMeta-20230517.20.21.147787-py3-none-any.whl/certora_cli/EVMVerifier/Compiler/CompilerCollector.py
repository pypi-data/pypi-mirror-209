from abc import abstractmethod, ABC
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union, Set
from Shared.certoraUtils import AbstractAndSingleton
import EVMVerifier.certoraType as CT


# TODO: merge this with Func in certoraBuild
class CompilerLangFunc:
    def __init__(self,
                 name: str,
                 fullargs: List[CT.TypeInstance],
                 paramnames: List[str],
                 returns: List[CT.TypeInstance],
                 sighash: str,
                 notpayable: bool,
                 fromlib: bool,  # not serialized
                 isconstructor: bool,  # not serialized
                 statemutability: str,
                 visibility: str,
                 implemented: bool,  # does this function have a body? (false for interface functions)
                 overrides: bool,  # does this function override an interface declaration or super-contract definition?
                 ast_id: Optional[int] = None,
                 where: Optional[Tuple[str, str]] = None  # 1st element: source file name, 2nd element: location string
                 ):
        self.name = name
        self.fullArgs = fullargs
        self.paramNames = paramnames
        self.returns = returns
        self.sighash = sighash
        self.notpayable = notpayable
        self.fromLib = fromlib
        self.isConstructor = isconstructor
        self.stateMutability = statemutability
        self.visibility = visibility
        self.where = where
        self.implemented = implemented
        self.ast_id = ast_id
        self.overrides = overrides


class CompilerLang(metaclass=AbstractAndSingleton):
    """
    This class represents the compiler-language property attached to [CompilerCollector].
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def compiler_name(self) -> str:
        pass

    @staticmethod
    def normalize_func_hash(func_hash: str) -> str:
        """
        Normalizes the hash [func_hash] (first 4 bites in a function's signature).
        """
        return func_hash

    @staticmethod
    def normalize_file_compiler_path_name(file_abs_path: str) -> str:
        """
        Normalizes the absolute path name [file_abs_path] of a file, given to the compiler.
        """
        return file_abs_path

    @staticmethod
    def normalize_deployed_bytecode(deployed_bytecode: str) -> str:
        """
        Normalizes the deployed bytecode [deployed_bytecode].
        """
        return deployed_bytecode

    @staticmethod
    @abstractmethod
    def get_contract_def_node_ref(contract_file_ast: Dict[int, Any], contract_file: str, contract_name: str) -> \
            int:
        """
        Given the AST [contract_file_ast], the contract-file [contract_file] and the contract [contract_name] inside
        [contract_file], returns the (expected to be single) definition node reference for [contract_name] which is
        located inside [contract_file_ast].
        """
        pass

    @staticmethod
    @abstractmethod
    def compilation_output_path(sdc_name: str, config_path: Path) -> Path:
        """
        Returns the path to the output file generated by the compiler for [sdc_name],
        using the given config path [config_path]. If several output files are generated by the compiler, returns the
        one that stores stdout.
        """
        pass

    @staticmethod
    @abstractmethod
    def all_compilation_artifacts(sdc_name: str, config_path: Path) -> Set[Path]:
        """
        Returns the set of paths for all files generated after compilation.
        """
        pass

    @staticmethod
    def collect_storage_layout_info(file_abs_path: str,
                                    config_path: Path,
                                    compiler_cmd: str,
                                    data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Returns the data dictionary of the contract with storage layout information if needed
        """
        return data

    @staticmethod
    @abstractmethod
    def get_supports_imports() -> bool:
        """
        Returns True if the language supports imports, False otherwise
        """
        pass

    @staticmethod
    @abstractmethod
    def collect_source_type_descriptions_and_funcs(asts: Dict[str, Dict[str, Dict[int, Any]]],
                                                   data: Dict[str, Any],
                                                   contract_file: str,
                                                   contract_name: str,
                                                   build_arg_contract_file: str) -> \
            Tuple[List[CT.Type], List[CompilerLangFunc]]:
        pass


class CompilerCollector(ABC):
    """
    This class incorporates all the compiler settings.
    Compiler-settings related computations should be done here.
    """

    @property
    @abstractmethod
    def compiler_name(self) -> str:
        pass

    @property
    def optimization_flags(self) -> str:
        return ""

    @property
    @abstractmethod
    def smart_contract_lang(self) -> CompilerLang:
        pass

    @property
    @abstractmethod
    def compiler_version(self) -> Union[str, Tuple[int, int, int]]:
        """
        For Solidity compiler, the version is expected to be of type
        Tuple[int, int, int], while for Vyper it is expected to be a string.
        """
        pass

    def __str__(self) -> str:
        return f"{self.compiler_name} {self.compiler_version}"
