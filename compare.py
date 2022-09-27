# reading files
f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")
f3 = open("file3.txt", "w")

i = 0

for line1 in f1:
	i += 1

	for line2 in f2:

		# matching line1 from both files
		if line1 == line2:
			# print IDENTICAL if similar
			print("Line ", i, ": IDENTICAL")
		else:
			f3.write(line1)
            f3.write("\n")
		break

# closing files
f1.close()
f2.close()
f3.close()
