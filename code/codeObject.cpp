# include "code/codeObject.hpp"
# include "object/hiString.hpp"

CodeObject::CodeObject(int argcount, int nlocals, int stacksize, int flag, HiString * bytecode,
            ArrayList<HiObject *> * consts, ArrayList<HiObject *> * names,
            ArrayList<HiObject *> * varnames,
            ArrayList<HiObject *> * freevar, ArrayList<HiObject *> * cellvars,
            HiString * file_name, HiString * co_name, int lineno, HiString * notable):
                _argcount(argcount),
                _nlocals(nlocals),
                _stack_size(stacksize),
                _flag(flag),
                _bytecodes(bytecode),
                _names(names),
                _consts(consts),
                _var_names(varnames),
                _free_vars(freevar),
                _cell_vars(cellvars),
                _co_name(co_name),
                _file_name(file_name),
                _lineno(lineno),
                _notable(notable){
}