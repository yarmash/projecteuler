#!/usr/bin/env perl

sub factorial {
	my ($n) = @_;

	my $f = 1;
	$f *= $_ for 1..$n;
	return $f;
}

sub nthPerm {
	my ($s, $n) = @_;

	my $len = length($s);
	return $s if $len < 2;

	my $perms = factorial($len-1);
	my $i = int($n / $perms);
	return substr($s, $i, 1, "") . nthPerm($s, $n - $i*$perms);
}

print nthPerm("0123456789", 999999);
