Our group includes Zhaoyang Meng, Yukun Bao, Li Zhang, Hongbo Wang

The project is about:

You are to get the raw NBA stats from the Web, compute the efficiency of 3924 players, and output the 50 most efficient players, as well as some other interesting statistics.

Your program is to take no input (except for reading the file) and produce a file that contains all the results.

NBA Data Collection and Manipulation

1. Goto	http://www.databasebasketball.com/stats_download.htm
2. Download  	databaseBasketball2.1.zip
3. Unpack the zip file (most machines will do this when you double-click the file)
4. We will only do statistics based on “player_regular_season_career.txt”. So copy this file into the same directory where you write your python program.

The format of this file is easy to understand. The first line tells you the names of all columns. From the second line, each line’s data corresponds to one player’s career regular season’s statistics. Each field is separated by “|”

We not only fulfill the targets, but also add some new functions: you can print all the top 50 in the program and search for the n-th best player.
