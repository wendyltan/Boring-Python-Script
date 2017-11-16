print """
You used to be an adventurer.Someone told you that there is a large amount of  money
on an unknown island and it is the time when you need the money most.
You also get to know that the bussinessman Jerry in town might have the map leading 
to the island.Would you like to visit Jerry today?The time seems a little late because the sky is getting dark.
1.Set off to Jerry's house now
2.No,it's too late.maybe tomorrow.
3.No, i have no interest in the misterious island at all.
"""

visit = raw_input("> ")
if visit == "1":
	print """
	You can take something with you before setting off,which would you choose?
	1.a very sharp knife. 
	2.a gun with only one bullet. 
	3. a cake which is tasty.
	"""

	take = raw_input("> ")
	if take == "1":
		print """
		You carry the knife with you.You know if you want to visit Jerry,
		you have to go through a forest,which may have potential danger in it.You walk as
		fast as you can to avoid meeting any trouble.There is an old woman just 
		suddenly appear along the narrow road in the dark forest.She seems to carry
		something bloody and walks real slow.Her face is paper white and she is asking you for help
		to get to her home for she has been injured by a dog.Would you like to 
		help her or not?It might be dangerdous but she seems too old to threaten you.
		1.Help her to her house.
		2.She is dangerous.I should kill her and run away with her stuff.
		3.Just ignore her.I don't have any time for this now.
		"""

		old = raw_input("> ")
		if old == "1":
			print """
			You help her to her house.She says thanks to you,smiling, and offer you a cup of coffee.
			You happily drink it all.Her face suddenly turns horribly and you fall down heavily
			on the ground.The old woman laugh loudly while playing a shining bloody thing on her
			hand but you can't see what it is already.You are poisoned by the
			evil old woman.You are dead. 
			"""
			raw_input("END:")
			print "Game over."
		elif old == "2":
			print """
			The woman can't fight against you and didn't think you will do this to her.
			Red knife is pulled out of her body and you give out a sigh with relief.
			You searh her stuff and found some green liquid in a tube ,writing
			\"toxicant,can cause an adult's death in 2 min,no cure.\"And also, you found that the bloody
			thing is in fact a silver key .you pick up the key and keep walking towards to the direction of Jerry's house.
			finally you arrive in front of his house.You knock at the door but nobody answer.you try with the key
			and suprisingly find it work!The door is opened and the sky is completly dark now.Would you like to search 
			for Jerry?
			1.yes,go search.
			2.no,i should go out of his home and wait him back.
			"""

			search = raw_input("> ")
			if search == "1":
				print """
				You find Jerry is lying on the floor at a dark corner with much blood covering him.
				You want to help him up but he can't get up anymore.He says,he was attacked by an old 
				woman with a knife in his house and forced to tell where the map is but he didn't tell 
				her at last so the woman robbed the key and went away,considering to search the house the other day.
				You tell him that the woman has been killed by you and there is no worries at all.Jerry feels both 
				surprise and happy.He lifts up his finger and points to a wooden case at the corner with difficulty.
				He says, the map is under the case,son. I hope you get what you want but be REALLY CAREFUL, the creature 
				on the island are evil so I wish you have prepared well....remember, the silver..is ..the.....he didn't 
				finish the word and passes away.You bury him at the front yard and decide to set off the other morning.
				"""
				raw_input("END:")
				print "TRUE END."
			else:
				print """
				As soon as you go out of the house, a man covering in blood just jump up near 
				the door and pull the triger.Bang!You die.Jerry put a bullet right through 
				your head.\"HaHaHa..want to kill me with the knife,huh?bitch?\"
				"""
				raw_input("END:")
				print "Game over."
		else:
			print """
			You ignore the strange woman and arrive in front of the door of Jerry's.
			You knock at the door but no one answer.You find that the door is unlocked
			so you walk staight through in it.Jerry is lying on the floor with much blood
			coming out of his body,unconsciously. You help him bandage his wound and help him up
			on his chair.After feeding him with some water,he wakes up and tell you that 
			an old strange woman just took his map to the island away and if you are coming
			for the map it may let you down.But he may know how to get to her house cause
			she had mentioned that she wanted the treassure to cure a man,Packie,Who is the famous
			person in the town.Jerry has never been to Packie's house but someone has told
			him how to go there.Now would you like to stay with Jerry or leave alone?
			1.stay with Jerry!
			2.leave alone.
			"""

			house = raw_input("> ")
			if house == "1":
				print """
				Ok,Jerry is planing to set off with you the other day morning.
				Jerry offers you with a few things might useful to you for tomorrow's battle,now which
				will you choose?
				1.a gun with silver bullets full loaded.
				2.an apple which seems to have magic power for it's shining.
				"""

				things = raw_input("> ")
				if things == "1":
					print """
					You choose a gun ,which is totally the wise choice.The morning soon come,
					and Jerry went to the Packie's house with you.Both of you sneak slowly
					close to the old woman's house,notcing she is making breakfast for sombody.
					Jerry gives you a signal by gesture,hinting you to move in the house and 
					killed the woman.The woman doen't notice your uninvited coming at all.you 
					move to her back and lift up the gun.
					1.Pull the triger.
					2.Hit the woman heavily.
					"""

					ways = raw_input("> ")
					if ways == "1":
						print """
						The woman fall in her own blood.Jerry comes in full of excitement and 
						yelling:give me the gun! then he loots your gun and go into the bedroom.
						bang!you hear a loud gunshot.And after a while, he came out with blood,
						which is not his.He stares at you in a strange way:\"well I have get the map
						back ,son.you are a good young man but you have known too much.I'm 
						sorry..nobody but me can have the treassure in this world!\"You try to escape
						but you are not faster than a bullet.So you die.
						"""
						raw_input("END:")
						print "Game over."
					else:
						print """
						You didn't kill her,no matter what, you are used to be an adventurer
						not the muderer or killer.But the woman is so tough that she fights back.
						She pours something green on your face.You give out a sad shrill cries
						that can be heard miles away.you find your face is melting down and so do other
						part of your body .\"hhh..you think you can rob me of the map?just you
						and the useless businessman?never!He was killed by my husband and now you are going 
						to be a puddle of liquid....\"
						"""
						raw_input("END:")
						print "Game over."
				else:
					print """
					Although not knowing what's it's use,you still thinks it's powerful
					.The morning soon come,and Jerry went to the Packie's house with you.both of you sneak 
					slowly close to the old woman's house,notcing she is making breakfast 
					for sombody.Jerry gives you a signal by gesture,hinting you to move in the house and 
					killed the woman.The woman doen't notice your uninvited coming at all.
					You move to her back give her head a punch.She falls on the floor as soon as Jerry comes
					in.He asks you to serach for the map.You go in the bedroom and 
					there is also a man,not even know if a human,with green skin,lying on the bed.He seems asleep
					and you don't want to kill anyone.So you search around him but find nothing.
					Suddenly he opens his dark and green eyes--which is definetely not any kind of eyes
					human can have and starts attacking you.You grap the knife taken from home 
					and stick it into strange creature's head.He stops moving,with green blood popping out.
					Luckily,you find the map under his legs.
					You go out to the place where Jerry should be,
					but he isn't there,neither is the old woman.Instead, a vomitive liquid is on the floor,
					along with a gun with silver bullets full loaded.You pick it up ,walk around and
					think the old woman must hasn't dead yet.While you are going to open the door of bathroom,
					the old woman pours something green on your face.You give out a sad shrill cries
					that can be heard miles away.You find your face is melting down and so 
					do other part of your body .\"hhh..you think you can rob me of the map?just you and the useless businessman?
					never!He was killed by me and now you are going to be a puddle of liquid....\"At this very moment,
					the apple shining automatically mix together with your body.The melting process
					stops and you heel in a very fast speed.\"No..!!!That is impossible!\"
					the old woman is shocked and standing still.\"This never fail before,but..\"
					You don't want to hear her bb anymore so you pull the triger.Bang!The old woman 
					dies with great shock in her face.You decide to go home first,and go to the island after few days...
					"""
					raw_input("END:")
					print "I'm ready."
			else:
				print """
				You get nothing and you are living a poor and boring life until you die lonely.
				"""
				raw_input("END:")
				print "Boring man."
	elif take == "2":
		print """
		You set off full of confident.But unfortunately you come across a strong bear on the way.
		One bullet makes no difference,too hard to kill the bear.So you are teared apart and eaten by wolfs
		in the forest.
		"""
		raw_input("END:")
		print "Game over."
	else:
		print """
		Seriously? What do you think a cake can do?Going outdoors for picnic?
		You are dead on the way by attacked by groups of army ants.--leading by the smell of your yummi cake.
		"""
		raw_input("END:")
		print "You make me laugh."

elif visit == "2":
	print """
	You go to Jerry's house,the door is unlocked.You hesitate for a while and decide to go in.
	You find a letter writing by blood:	
	\"The map was robbed by an evil woman,who has something to do with the misterious island.
	She must want to own the tressure herself!Who see this letter please help me!Get the map of island back.
	Although I'm dying..But you can own them,the treassure,all!
	Here is her address:xxxXX.JERRY'S LAST WORD.\"So will you trust his words and 
	find the map?
	1.No,..too dangerdous.Life is more valuable than so called bullshit treassure..
	2.Why not?Going to the treassure island is what i always want!
	"""
	findmap = raw_input("> ")
	if findmap == "1":
		print """
		you get nothing and you are living a poor and boring life until you die lonely.
		"""
		raw_input("END:")
		print "Boring man."
	else:
		print """
		You get there, but find that it is just an empty house,nothing but some green 
		liquid loading in tubes left on the table.You are very disappointed
		and want to leave.Do you want to take the tubes with you?
		1.Yes, don't want to be empty hand.
		2.No,just leave.
		"""

		tubes = raw_input("> ")
		if tubes == "1":
			print """
			You go home ,live like nothing had happened,until one day you accidentally 
			knock over the tubes and the green liquid covers on you
			...you become a puddle of liquid,dead,completely.
			"""
			raw_input("END:")
			print "Don't be so greedy."
		else:
			print """
			You get nothing and you are living a poor and boring life until you die lonely.
			You always regret that why you didn't set
			off earlier that day.
			"""
			raw_input("END:")
			print "Time not waits."
else:
	print """
	You didn't go for your dream.But you marry soon and have a happy life with your family.
	"""
	raw_input("END:")
	print "Really happy?"
 


print "Thanks for playing the 1/3 part of the game!Hit any keys to exit."
raw_input(">>")









