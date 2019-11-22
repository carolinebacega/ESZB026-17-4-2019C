#!/bin/sh
ARQUIVODADOS=/home/pi/sist_embarcados_git/lab07/gnuplot/dados.txt
ARQUIVOSAIDA=/home/pi/sist_embarcados_git/lab07/gnuplot/dados.png

gnuplot << EOF
set title "Título"
set ylabel "Eixo Y"
set xlabel "Eixo X"
set terminal png
set output "$ARQUIVOSAIDA"
plot "$ARQUIVODADOS" \
     linecolor rgb '#ffd8b1' \
     linetype 3 \
     linewidth 2 \
     pointtype 19 \
     pointsize 1.0 \
     title "meus dados" \
     with linespoints
EOF

