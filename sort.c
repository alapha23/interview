#include "sort.h"

int main(void)
{
	int counter = 0;
	
	open_partition();
	traversal();

	/*
	 * Find largest and minimum element in the whole dataset
	 * It wouldn't be complicated since we have only 256 partition
	 *	[min, max] = traversal(whole_data)
	 * We presume it is dividable
	*/

	while(counter < num_partition - 1)
	{
		if((pid[counter]=fork())==0)
		{   
			partition_id = counter;
		/*  
		 *  Load partition into memeory
		 *  Type of partition should be 2d list 
		 *  It contains 1024 data blocks in which each one has 8000 int64
		*/
			parition_list = read_partition(partition_id);
			upper_bound = (partition_id+1) * interval;
			lower_bound = partition_id * interval;	
			/* We would like to separate data outside this bound to other process */
			for block_id in range(0, blocks_each_partition){
				if( upper_bound < partition_list[block_id].min || lower_bound > partition_list[block_id].max){
					target_id = floor(partition_list[block_id].min / interval);                     
					send_to_proper_process(partition_list[block_id], block_id, target_id);
					remove_from_partition(partition_list[block_id], block_id, target_id)                                ;
				/*  For one thing, shared memory could be a good approach 
				 *  since we could pass an address to another process instead of free the memory in this process
				 *  For another, save the data block to disk, so that other process do not have to wait for the signal to arrive
				 * 
				 */
				}
				else{
		      			[remains, send] = seperate_block(partition_list[block_id], upper_bound, lower_bound);
					replace_block(partition_list, block_id, remains);
					target_id = floor(send.min / interval);
					send_to_proper_process(send, block_id, target_id);
				}
			}
			save_to_disk(partition, partition_id);
			exit(0);
		}
	        counter++;
		wait_all();

	/*
	 * Since many processes exit instead of waiting for a signal during execution time
	 * Data blocks are stored at disk
	 * We merge the blocks into the partiion
	*/
	merge_fragments();
	return 0;
}
