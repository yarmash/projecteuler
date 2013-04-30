#!/usr/bin/perl

use Mojo::Base -strict;#
use Mojo::UserAgent;


sub fetch_problem {
	my ($n) = @_;

	my $ua = Mojo::UserAgent->new;
	my $dirname = sprintf "%03d", $n;
	say $dirname;

	if (-d $dirname) {
		return 1;
	}

	mkdir $dirname;

	open my $fh, ">", "$dirname/readme" or die $!;

	my $url = "https://projecteuler.net/problem=$n";
	my $tx = $ua->get($url);

	if (my $res = $tx->success) {
		my $dom = $res->dom;

		$dom->find("h2")->each(sub {
			my $h2 = $_[0]->all_text;
			printf $fh "%s\n%s\n\n", $h2, "=" x length($h2);
		});

		$dom->find("div.info h3")->each(sub {
			printf $fh "%s\n\n", $_[0]->all_text;
		});

		$dom->find("div.problem_content")->each(sub {
			printf $fh "%s\n", $_[0]->all_text;
		});
	}
	else {
		my ($err, $code) = $tx->error;
		die $code ? "$code response: $err" : "Connection error: $err";
	}
	return 1;
}

my $n = 1;
1 while fetch_problem($n++);
