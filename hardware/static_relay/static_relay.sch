EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:Conn-raspberry
LIBS:static_relay-cache
EELAYER 24 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "static relay"
Date "20 may 2013"
Rev "1"
Comp "JbLb for Haum"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L TRIAC U1
U 1 1 51992C6F
P 10000 2450
F 0 "U1" H 9750 2800 70  0000 C CNN
F 1 "TRIAC" H 9700 2200 60  0000 C CNN
F 2 "" H 10000 2450 60  0001 C CNN
F 3 "" H 10000 2450 60  0001 C CNN
	1    10000 2450
	1    0    0    -1  
$EndComp
$Comp
L R R1
U 1 1 51992C75
P 9000 2050
F 0 "R1" V 9080 2050 50  0000 C CNN
F 1 "470" V 9000 2050 50  0000 C CNN
F 2 "" H 9000 2050 60  0001 C CNN
F 3 "" H 9000 2050 60  0001 C CNN
	1    9000 2050
	0    1    1    0   
$EndComp
$Comp
L MOC3022M IC1
U 1 1 51992C78
P 8250 2550
F 0 "IC1" H 8036 2729 40  0000 C CNN
F 1 "MOC3022M" H 8350 2365 40  0000 C CNN
F 2 "DIP6" H 8086 2375 29  0000 C CNN
F 3 "" H 8250 2550 60  0001 C CNN
	1    8250 2550
	1    0    0    -1  
$EndComp
$Comp
L CONN_2 P1
U 1 1 51992D60
P 7450 2550
F 0 "P1" V 7400 2550 40  0000 C CNN
F 1 "CONN_2" V 7500 2550 40  0000 C CNN
F 2 "" H 7450 2550 60  0001 C CNN
F 3 "" H 7450 2550 60  0001 C CNN
	1    7450 2550
	-1   0    0    -1  
$EndComp
$Comp
L CONN_1 P2
U 1 1 51992D72
P 7500 1300
F 0 "P2" H 7580 1300 40  0000 L CNN
F 1 "CONN_1" H 7500 1355 30  0001 C CNN
F 2 "~" H 7500 1300 60  0000 C CNN
F 3 "~" H 7500 1300 60  0000 C CNN
	1    7500 1300
	-1   0    0    1   
$EndComp
$Comp
L CONN_1 P3
U 1 1 51992D81
P 7500 1550
F 0 "P3" H 7580 1550 40  0000 L CNN
F 1 "CONN_1" H 7500 1605 30  0001 C CNN
F 2 "~" H 7500 1550 60  0000 C CNN
F 3 "~" H 7500 1550 60  0000 C CNN
	1    7500 1550
	-1   0    0    1   
$EndComp
Wire Wire Line
	9500 2650 8600 2650
Wire Wire Line
	10000 2050 9250 2050
Wire Wire Line
	8750 2050 8600 2050
Wire Wire Line
	8600 2050 8600 2450
Wire Wire Line
	7650 1550 10000 1550
Wire Wire Line
	10000 1550 10000 2050
Wire Wire Line
	7650 1300 10400 1300
Wire Wire Line
	10400 1300 10400 2700
Wire Wire Line
	10400 2700 10000 2700
Wire Wire Line
	7800 2450 7900 2450
Wire Wire Line
	7900 2650 7800 2650
$EndSCHEMATC
