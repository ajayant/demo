#/demo

read -p "Select Insert/Search/Delete: " x

if [ $x == 'Insert' ] || [ $x == 'insert' ]
then
	python helper.py
fi
if [ $x == 'search' ] || [ $x == 'Search' ] ||
   [ $x == 'Delete' ] || [ $x == 'delete' ] 
then 
	python print_buckets.py
fi
