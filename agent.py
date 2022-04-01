import numpy as np
import pandas as pd
from canvas import Canvas


class AgentRL:
    def __init__(self, actions, learn_speed=0.03, influence_decay_coeff=0.9, major_prob=0.9):
        self.actions = actions
        self.speed = learn_speed
        self.gamma = influence_decay_coeff
        self.epsilon = major_prob
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
       

    def chooseAction(self, observation):
        self.check_state(observation)
        if np.random.uniform() < self.epsilon:
            s_action = self.q_table.loc[observation, :]
            action = np.random.choice(
                s_action[s_action == np.max(s_action)].index)
          
        else:
            action = np.random.choice(self.actions)
        return action

    def learn_strategy(self, cur_state, action, reward, next_state):
        self.check_state(next_state)
       
        q_predict = self.q_table.loc[cur_state, action]
        if next_state != 'terminal':
            #print(reward)
            q_target = reward + self.gamma * \
                self.q_table.loc[next_state, :].max()
            #print(q_target)
        else:
            q_target = reward
        self.q_table.loc[cur_state, action] = self.q_table.loc[cur_state,
                                                               action]+self.speed * (q_target - q_predict)
    
    # Helper method
    def check_state(self, state):
        print(self.q_table)
        if state not in self.q_table.index:
          
            self.q_table = self.q_table.append(
                pd.Series(
                    [0]*len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
                
            )



def update():
    for episode in range(100):
        obs = env.reintialize()
        while 1:
            env.render()
            act = ai.chooseAction(str(obs))
            obs_, reward, over = env.random_move(act)
            ai.learn_strategy(str(obs), act, reward, str(obs_))
            obs = obs_
            if over:
                break
    print("Round is over you reach 100 episode")
    env.destroy()


if __name__ == "__main__":
    env = Canvas()
    ai = AgentRL(actions=list(env.actions))

    env.after(100, update)
    env.mainloop()
