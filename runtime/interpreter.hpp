# ifndef INTERPRETER_HPP
# define INTERPRETER_HPP

# include "code/bytecode.hpp"
# include "code/codeObject.hpp"


class Interpreter {
    private:
        HiObject * _exception_class;
        ArrayList<HiObject *> * _consts;
        ArrayList<HiObject *> * _stack;


    public:
        void run(CodeObject * codes);
};

# endif