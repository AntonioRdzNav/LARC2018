#ifndef _Movimiento_h
#define _Movimiento_h
#include <_BNO055.h>
#include <_ColorSensor.h>
#include <_Encoder.h>
#include <_LibraryPID.h>
#include <_Motors.h> 
#include <_Sharp.h>
#include <_TimeFlight.h>
#include <_TCRT5000.h>
#include <_LCD.h>

class _Movements{
    public:
// TODO: METHODS
        void setupMovements();
        // Modular functions
        void updateSensors(bool, bool, bool, bool, bool, bool);
        void movePID(bool, char);
        void spinPID(bool, double);
        void turnPID(bool);        
        // Get Angle Outputs
        void setBaseVelocitiesByDirection(bool, char);
        void setBaseSpecificVelocities(double, double, double, double);
        void calculateAngleOutputsByDirection(bool, char);
        void verifyAndUploadOutputsByDirection(char);
        void verifySpecificAndUploadOutputs(double, double);
        // Move n Time/CM
        void movePID_nSec(double, bool, char);
        void movePID_nCM(double, bool, char);        
        // Align using TOF PID
        void align_tof();        
        void larc_alignToPickContainer(int);
        // Align using TCRT5000 PID
        void larc_alignBetweenVerticalBlackLine(bool, char);
        char oppositeDirection(char);
        void larc_alignToShip(bool, char);
        void larc_moveUntilBlackLine(bool, char, bool, bool, bool);
// TODO: ATTRIBUTES
        _BNO055 *bno055;
        _ColorSensor *colorSensor;
        _Encoder *encoder;
        _LibraryPID *pid;
        _Motors *motors;
        _Sharp *sharp;
        _TimeFlight *timeFlight;
        _TCRT5000 *tcrt5000;
        _LCD *lcd;
};

#endif