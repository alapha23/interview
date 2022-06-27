#ifndef __SORT__
#define __SORT__

#include <stdio.h>
#include <stdlib.h>


#define int64	long long

struct block
{
	int64 ** data;
	int64	min;
	int64	max;
};

/* number of processes also is num_partition */
#define num_partition  256
#define blocks_each_partition 1024;

char file_dir[] = "data/segment_";
long long global_max = 0;
long long global_min = 0;
int partition_fd[num_partition];
int all_pid[num_partition];

void open_partition(int partition_id)
{
	;
}
void close_partition(){;}

void traversal(void)
{
	;
}

static int open_file(char *filename)
{}
#endif
