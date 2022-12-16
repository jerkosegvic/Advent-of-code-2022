#!/usr/bin/perl

# Modules used
use strict;
use warnings;
use List::Util qw( min max );


my $filename = 'sample';

open(FH, '<', $filename) or die $!;
my $sol = 0;
my $curr = 0;
my @stack = ();
my @list_of_directories = ();

while(<FH>){
    my $tren = $_;
    $tren=~ s/^\s+|\s+$//g;
    if ($tren eq '$ cd ..'){
        if(@stack[$curr] < 100000){
            $sol += @stack[$curr];
        }
        push(@list_of_directories , @stack[$curr]);
        $curr -= 1;
        @stack[$curr] += @stack[$curr + 1];
        next;
    }
    if( index($tren, 'dir') == 0 or $tren eq '$ ls'){
        next;    
    }
    if( index($tren, '$ cd') == 0){
        $curr +=1;
        @stack[$curr] = 0;
    }
    else {
        my @words = split / /, $tren;
        my $broj = int(@words[0]);
        @stack[$curr] += $broj;
    }
    #print $tren;
}

my $sum = 0;
for(my $i = $curr; $i >= 0; $i--){
	$sum += @stack[$i];	
    push(@list_of_directories , $sum) 
}

my $need = max @list_of_directories;
my @list_of_directories_to_delete = grep { $_ >= 30000000 - ( 70000000 - $need )} @list_of_directories;
my $izbaci = min @list_of_directories_to_delete;

print "izbaci je $izbaci \n";
print "$sol \n";
close(FH);
