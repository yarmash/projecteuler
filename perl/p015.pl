#!/usr/bin/env perl

use strict;
use warnings;

my ($N, @dp) = (20, [1]);

for my $row (0..$N) {
    for my $col (0..$N) {
        $dp[$row][$col] += $dp[$row-1][$col] if $row;
        $dp[$row][$col] += $dp[$row][$col-1] if $col;
    }
}

print($dp[-1][-1], "\n");
