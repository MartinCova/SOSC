set encoding utf8
set termoption noenhanced
set title "* inverter 2 transistors"
set xlabel "s"
set ylabel "V"
set grid
unset logscale x 
set xrange [0.000000e+00:2.500000e-06]
unset logscale y 
set yrange [-8.176244e-02:1.875265e+00]
#set xtics 1
#set x2tics 1
#set ytics 1
#set y2tics 1
set format y "%g"
set format x "%g"
plot 'in.data' using 1:2 with lines lw 1 title "out"
