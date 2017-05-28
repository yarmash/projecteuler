#!/usr/bin/env perl

use strict;
use warnings;

sub sum_digits {
    my ($num) = @_;
    my $sum = 0;

    while ($num) {
        $sum += $num % 10;
        $num /= 10;
    }
    return $sum;
}

sub main {
    my $cnt = 0;
    my $num_digits = 2;

    while (1) {
        my $max_num = 10 ** $num_digits;
        my $min_num = $max_num / 10;

        for my $digit_sum (2 .. $num_digits*9) {
            my $num = $digit_sum * $digit_sum;
            my $power = 2;

            while ($num < $max_num) {
                if ($num >= $min_num && $num < $max_num && $num == sum_digits($num) ** $power) {
                    return $num if ++$cnt == 30;
                }
                $num *= $digit_sum;
                $power++;
            }
        }
        $num_digits++;
    }
}

print(main, "\n");
