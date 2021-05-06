# ifndef _HI_INTEGER_HPP
# define _HI_INTEGER_HPP

# include "object/hiObject.hpp"

class HiInteger : public HiObject{
    private:
        int _value;

    public:
        HiInteger(int x) { _value = x; }
        int value() { return _value; }
        HiObject * add(HiObject *);
        void print();

        HiObject * greater(HiObject *);
        HiObject * less(HiObject *);
        HiObject * equal(HiObject *);
        HiObject * not_equal(HiObject *);
        HiObject * ge(HiObject *);
        HiObject * le(HiObject *);
};

# endif