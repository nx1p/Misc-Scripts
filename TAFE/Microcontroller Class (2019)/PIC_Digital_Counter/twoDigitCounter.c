/**
 *		                Digital Counter
 *                 =-=-=-=-=-=-=-=-=-=-=-=-=-=
 *   This simple program is designed for the PIC18F45K22. 
 *   It counts from zero to ninety-nine, displaying the count on two 7-segment modules.
 *
 *
 * Author:    Marceline Kuo-Arrigo
 * Created:   28.05.2019
 **/
 
 
 
//Declare counting variables and look up table
int ones=0;
int tens=0;
const int number_pattern[10] = {0x81,0xED,0x43,0x49,0x2D,0x11,0x10,0xCD,0x01,0x08};

/*
# display_number function
Accepts two parameters, first parameter is the number to be displayed.
Second parameter is which register to write to.
0 selects the segment on the left, the ones segment.
1 selects the segment on the right, the tens segment.

Example usage:
    display_number(9,0);
                   ^ ^   Writes the number nine to the ones segment
*/
void display_number(int i, int r) {
    LATD=number_pattern[i];
    switch(r){
        case 0:
            LATC=0x02;
            break;
        case 1:
            if (LATD==number_pattern[0]) LATD=0xFF;
            LATC=0x01;
            break;
    }
    LATC=0x00;
}

/* Initialises timer0 interrupt for 250ms using values,
   conveniently calculated by the timer calculator program,
   available for free online from Mikroelektronika
   https://www.mikroe.com/timer-calculator
*/
void InitTimer0(){
  T0CON  = 0x82;
  TMR0H  = 0x0B;
  TMR0L  = 0xDC;
  GIE_bit    = 1;
  TMR0IE_bit     = 1;
}

// Main code
void Interrupt(){
  if (TMR0IF_bit){ // Only runs this section of code if the interrupt was timer0 
  
    TMR0IF_bit = 0; // Resets the timer0 flag bit
    TMR0H    = 0x0B;
    TMR0L    = 0xDC;
    
    /* 
        This section increments the ones counter unless if the ones counter has reached nine.
        
        If it has, it resets the ones counter and increments the tens counter,
        unless the tens counter is also nine.
        If so, then it resets the tens counter instead.
    */
    if(ones == 9){
        ones=0;
        
        if (tens==9) tens=0;
        else if (tens!=9) tens++;
    }
    else if (ones != 9) ones++;
    
    /* Write the tens and ones counter to the segments, whatever they may be*/
    display_number(tens,1);
    display_number(ones,0);
  }
} 

void main() {
    TRISC=0x00; //Sets Port C as outputs
    TRISD=0x00; //Sets Port D as outputs
    LATC=0x00; //Clears Port C to make sure it's 0.
    
    /* Sets Port C & D to digital to make sure there's no unexpected behaviour. */
    ANSELC=0;
    ANSELD=0;
    
    InitTimer0(); // Initialises timer0 interrupt
    
    /* Loop forever doing nothing until interrupted */
    for(;;){
    }
}