import gym
import numpy as np

env = gym.make('CartPole-v1')

LEARNING_RATE = 0.1
DISCOUNT = 0.95
RUNS = 10000
SHOW_EVERY = 100
epsilon = 0.1


def create_bins_and_q_table():
	numBins = 20
	obsSpaceSize = len(env.observation_space.high)

	bins = [
		np.linspace(-4.8, 4.8, numBins),
		np.linspace(-4, 4, numBins),
		np.linspace(-.418, .418, numBins),
		np.linspace(-4, 4, numBins)
	]

	qTable = np.zeros([numBins] * obsSpaceSize + [env.action_space.n])

	return bins, obsSpaceSize, qTable


def get_discrete_state(state, bins, obsSpaceSize):
	stateIndex = []
	for i in range(obsSpaceSize):
		stateIndex.append(np.digitize(state[i], bins[i]) - 1)
	return tuple(stateIndex)


bins, obsSpaceSize, qTable = create_bins_and_q_table()

for run in range(RUNS):
	discreteState = get_discrete_state(env.reset(), bins, obsSpaceSize)
	done = False

	while not done:
		if run % SHOW_EVERY == 0:
			env.render()

		if np.random.random() > epsilon:
			action = np.argmax(qTable[discreteState])
		else:
			action = np.random.randint(0, env.action_space.n)
		newState, reward, done, _ = env.step(action)

		newDiscreteState = get_discrete_state(newState, bins, obsSpaceSize)

		maxFutureQ = np.max(qTable[newDiscreteState])
		currentQ = qTable[discreteState + (action,)]

		newQ = (1 - LEARNING_RATE) * currentQ + LEARNING_RATE * (reward + DISCOUNT * maxFutureQ)
		qTable[discreteState + (action,)] = newQ
		discreteState = newDiscreteState

env.close()
