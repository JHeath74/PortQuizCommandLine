import ctypes

CorrectAnswersPortDict = {}
IncorrectAnswersPortDict = {}


def CorrectIncorrectResponses(playername, portpoints):
	response = -1

	while response != 0:
		response = input("Do you wish to see the correct or incorrect answers?\n"
						+ "1 for Correct Answers\n"
						+ "2 for Incorrect Answers\n"
						+ "0 for Exit\n")
		if response == "0":
			final_score(playername, portpoints)
			break
		if response == "1":
			print("Correct Guesses")
			for key, value in CorrectAnswersPortDict.items():
				#print("Port: {} - Portocol: {}\n".format(key, value))
				ctypes.windll.user32.MessageBoxW(0, "Port: {} - Portocol: {}\n".format(key, value), "Correct Guesses", 1)


		if response == "2":
			print("Incorrect Guesses")
			for key, value in IncorrectAnswersPortDict.items():
				print("Port:{} - Portocol: {}\n".format(key, value))


def final_score(playername, portpoints):
	file_name = playername + "Score" + ".txt"

	print("Saving your award certificate: " + file_name)

	awardtext = "Congratulations, " + playername + "\n" \
				+ "Final Score: " + str(portpoints) + "\n"
	final_score_award = open(file_name, "w")

	final_score_award.write(awardtext)

	final_score_award.write("\nCorrect Answers\n")

	for key, value in CorrectAnswersPortDict.items():
		final_score_award.write("Port:{} - Portocol: {}\n".format(key, value))

	final_score_award.write("\nIncorrect Answers\n")

	for key, value in IncorrectAnswersPortDict.items():
		final_score_award.write("Port:{} - Portocol: {}\n".format(key, value))

