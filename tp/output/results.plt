set encoding utf8
set termoption noenhanced
set title "* inverter 2 transistors"
set xlabel "s"
set grid
unset logscale x 
set xrange [1.000000e-12:2.500000e-06]
unset logscale y 
set yrange [-9.593975e-02:1.890283e+00]
#set xtics 1
#set x2tics 1
#set ytics 1
#set y2tics 1
set format y "%g"
set format x "%g"
plot '../output/results.data' using 1:2 with lines lw 1 title "a",\
'../output/results.data' using 3:4 with lines lw 1 title "y",\
'../output/results.data' using 5:6 with lines lw 1 title "i(vdd)*vdd"
