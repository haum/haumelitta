EESchema Schematic File Version 2  date dim. 19 mai 2013 22:09:36 CEST
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
LIBS:static_relay-cache
LIBS:pwr_lampe-cache
EELAYER 24 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "static relay"
Date "19 may 2013"
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
P 4500 2150
F 0 "U1" H 4250 2500 70  0000 C CNN
F 1 "TRIAC" H 4200 1900 60  0000 C CNN
F 2 "" H 4500 2150 60  0001 C CNN
F 3 "" H 4500 2150 60  0001 C CNN
	1    4500 2150
	1    0    0    -1  
$EndComp
$Comp
L R R1
U 1 1 51992C75
P 3500 1750
F 0 "R1" V 3580 1750 50  0000 C CNN
F 1 "470" V 3500 1750 50  0000 C CNN
F 2 "" H 3500 1750 60  0001 C CNN
F 3 "" H 3500 1750 60  0001 C CNN
	1    3500 1750
	0    1    1    0   
$EndComp
$Comp
L MOC3022M IC1
U 1 1 51992C78
P 2750 2250
F 0 "IC1" H 2536 2429 40  0000 C CNN
F 1 "MOC3022M" H 2850 2065 40  0000 C CNN
F 2 "DIP6" H 2586 2075 29  0000 C CNN
F 3 "" H 2750 2250 60  0001 C CNN
	1    2750 2250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4300 4550 4300 3950
$Comp
L CONN_2 P1
U 1 1 51992D60
P 1950 2250
F 0 "P1" V 1900 2250 40  0000 C CNN
F 1 "CONN_2" V 2000 2250 40  0000 C CNN
F 2 "" H 1950 2250 60  0001 C CNN
F 3 "" H 1950 2250 60  0001 C CNN
	1    1950 2250
	-1   0    0    -1  
$EndComp
$Comp
L CONN_1 P2
U 1 1 51992D72
P 2000 1000
F 0 "P2" H 2080 1000 40  0000 L CNN
F 1 "CONN_1" H 2000 1055 30  0001 C CNN
F 2 "~" H 2000 1000 60  0000 C CNN
F 3 "~" H 2000 1000 60  0000 C CNN
	1    2000 1000
	-1   0    0    1   
$EndComp
$Comp
L CONN_1 P3
U 1 1 51992D81
P 2000 1250
F 0 "P3" H 2080 1250 40  0000 L CNN
F 1 "CONN_1" H 2000 1305 30  0001 C CNN
F 2 "~" H 2000 1250 60  0000 C CNN
F 3 "~" H 2000 1250 60  0000 C CNN
	1    2000 1250
	-1   0    0    1   
$EndComp
Wire Wire Line
	4000 2350 3100 2350
Wire Wire Line
	4500 1750 3750 1750
Wire Wire Line
	3250 1750 3100 1750
Wire Wire Line
	3100 1750 3100 2150
Wire Wire Line
	2150 1250 4500 1250
Wire Wire Line
	4500 1250 4500 1750
Wire Wire Line
	2150 1000 4900 1000
Wire Wire Line
	4900 1000 4900 2400
Wire Wire Line
	4900 2400 4500 2400
Wire Wire Line
	2300 2150 2400 2150
Wire Wire Line
	2400 2350 2300 2350
$EndSCHEMATC
