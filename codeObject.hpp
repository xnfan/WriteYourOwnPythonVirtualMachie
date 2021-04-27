# ifndef CODE_OBJECT_HPP
# define CODE_OBJECT_CPP

# include "hiObject.hpp"

class HiString;

template <typename T>
class ArrayList;

class CodeObject{
    private:
        int _argcount;
        int _nlocals;
        int _stack_size;
        int _flag;

        HiString * _bytecodes;
        ArrayList<HiObject *> * _consts;
        ArrayList<HiObject *> * _names;
        ArrayList<HiObject *> * _var_names;
        
        ArrayList<HiObject *> * _free_vars;
        ArrayList<HiObject *> * _cell_vars;

        HiString * _co_name;
        HiString * _file_name;

        int _lineno;
        HiString * _notable;

        CodeObject(int argcount, int nlocals, int stacksize, int flag, HiString * bytecode,
            ArrayList<HiObject *> * consts, ArrayList<HiObject *> * names,
            ArrayList<HiObject *> * varnames,
            ArrayList<HiObject *> * freevar, ArrayList<HiObject *> * cellvars,
            HiString * file_name, HiString * co_name, int lineno, HiString * notable);

};

# endif