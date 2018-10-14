#ifndef _Logic_h
#define _Logic_h
#include <_Traductor.h>
#include <Arduino.h>

class _Logic{
    private:
        int *stacks;
        uint8_t blue_boxes, green_boxes;
        uint8_t lastStack;
        uint8_t firstRed;      
        char lastColor;
    
    public:
        _Logic();

        char verifyColor(char c);
        char handleRed();
        char grabContainer(char c);
        void stackToShip();
        void shipToStack(char c);

        _Traductor *traductor;  
        
};

#endif