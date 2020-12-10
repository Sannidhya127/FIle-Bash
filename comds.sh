mkfifo "$1.pipe"
id="$1.pipe"
command="$2"
user="$3"
service="$4"

# Test to see if user entered init
if [ "$command" = "init" ]; then
	echo "$id $command $user " > server.pipe
	read input < "$id"
	echo "$input"

# Test to see if user entered insert
elif [ "$command" = "insert" ]; then
	# Prompt user to enter credentials and read credentials.
	echo "Please Enter Login: "
	read login
	echo "Please Enter Password"
	read -s password
	# Encrypt the payload
	encrypt="$(printf "$login\n$password\n" | openssl enc -e -aes-256-cbc -a -salt)"
        echo "$id $command $user $service $encrypt" > server.pipe
        read input < "$id"
        echo "$input"

# Test to see if user entered show
elif [ "$command" = "show" ]; then
        echo "$id $command $user $service " > server.pipe
        read input < "$id"
	#decrypt the payload
	pay="$(echo "$input" | openssl aes-256-cbc -d -a)"
	for line in "$pay"; do
		echo "$line"
	done

# Test to see if user entered rm
elif [ "$command" = "rm" ]; then
        echo "$id $command $user $service" > server.pipe
        read input < "$id"
        echo "$input"

# Test to see if user  entered shutdown
elif [ "$command" = "shutdown" ]; then
        echo "$id $command" > server.pipe
	 read input < "$id"
	 echo "$input"

# Test to see if user  entered ls
elif [ "$command" = "ls" ]; then
	if [ "$#" -eq 3 ]; then
        	echo " $id $command $user " > server.pipe
	else
		echo " $id $command $user/$service " > server.pipe
	fi
	 while read input;do
        	echo "$input"
	done < "$id"

# Test to see if user entered edit
elif [ "$command" = "edit" ]; then
	#show ussers password
        echo "$id show $user $service" > server.pipe
	read input <"$id"

	#create file to edit payload
	tempdir=$(mktemp -d tmp.XXXXXXXXXX)
	tempfile=$(mktemp -p "$tempdir")

	# decrypt payload
	echo "$input" | openssl aes-256-cbc -d -a > tmp.XXXXXXXXXX
	nano tmp.XXXXXXXXXX

	encrypt="$(cat tmp.XXXXXXXXXX  | openssl enc -e -aes-256-cbc -a -salt)"
	# use contents of edited file to be used to update payload
	echo " $id update $user  $service $encrypt" > server.pipe
        read input < "$id"
        echo "$input"
	rm tmp.XXXXXXXXXX
	rm -r "$tempdir"
fi
rm "$1.pipe"

