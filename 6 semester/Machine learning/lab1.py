import torch
import seaborn as sns
import matplotlib.pyplot as plt


class Zscore:
	def __init__(self, tensor: torch.Tensor):
		self.mean = tensor.mean()
		self.sigma = tensor.std()

	def get_score(self, x):
		return (x - self.mean) / self.sigma

	def get_avarage_score(self, x):
		return torch.Tensor((x - self.mean) / self.sigma).mean()


"""Загружаємо датасет"""
tips = sns.load_dataset("tips")  # 'total_bill', 'smoker', 'time', 'size'

"""Вибираємо дані по курцях"""
smoker_total_bill = tips[tips['smoker'] == 'Yes']['total_bill'].values
smoker_size = tips[tips['smoker'] == 'Yes']['size'].values
nonsmoker_total_bill = tips[tips['smoker'] == 'No']['total_bill'].values
nonsmoker_size = tips[tips['smoker'] == 'No']['size'].values

"""Вибираємо дані по часу"""
dinner_total_bill = tips[tips['time'] == 'Dinner']['total_bill'].values
dinner_size = tips[tips['time'] == 'Dinner']['size'].values
lunch_total_bill = tips[tips['time'] == 'Lunch']['total_bill'].values
lunch_size = tips[tips['time'] == 'Lunch']['size'].values

"""Ініціалізація тензорів"""
tensor_total_bill = torch.Tensor(tips['total_bill'])
tensor_size = torch.Tensor(tips['size'])

tensor_smoker_total_bill = torch.Tensor(smoker_total_bill)
tensor_nonsmoker_total_bill = torch.Tensor(nonsmoker_total_bill)
tensor_smoker_size = torch.Tensor(smoker_size)
tensor_nonsmoker_size = torch.Tensor(nonsmoker_size)

tensor_dinner_total_bill = torch.Tensor(dinner_total_bill)
tensor_lunch_total_bill = torch.Tensor(lunch_total_bill)
tensor_dinner_size = torch.Tensor(dinner_size)
tensor_lunch_size = torch.Tensor(lunch_size)

"""Ініціалізація оцінки"""
score_total_bill = Zscore(tensor_total_bill)
score_size = Zscore(tensor_size)

score_smoker_total_bill = Zscore(tensor_smoker_total_bill)
score_nonsmoker_total_bill = Zscore(tensor_nonsmoker_total_bill)
score_smoker_size = Zscore(tensor_smoker_size)
score_nonsmoker_size = Zscore(tensor_nonsmoker_size)

score_dinner_total_bill = Zscore(tensor_dinner_total_bill)
score_lunch_total_bill = Zscore(tensor_lunch_total_bill)
score_dinner_size = Zscore(tensor_dinner_size)
score_lunch_size = Zscore(tensor_lunch_size)

"""Візуалізація Zscore для total_bill"""
total_bill_plot = sns.scatterplot(x=tensor_total_bill, y=tips['size'],
								  hue=(score_total_bill.get_score(tensor_total_bill).abs() > 3))
plt.xlabel('total_bill')
plt.ylabel('size')
plt.show()

"""Візуалізація Zscore для size"""
size_plot = sns.scatterplot(x=tensor_size, y=tips['total_bill'], hue=(score_size.get_score(tensor_size).abs() > 3))
plt.xlabel('size')
plt.ylabel('total_bill')
plt.show()

"""Візуалізація Zscore для total_bill серед курців"""
smoker_total_bill_plot = sns.scatterplot(x=tensor_smoker_total_bill, y=smoker_size,
										 hue=(score_smoker_total_bill.get_score(tensor_smoker_total_bill).abs() > 3))
plt.xlabel('smoker_total_bill')
plt.ylabel('smoker_size')
plt.show()

"""Візуалізація Zscore для total_bill серед некурців"""
nonsmoker_total_bill_plot = sns.scatterplot(x=tensor_nonsmoker_total_bill, y=nonsmoker_size,
											hue=(score_nonsmoker_total_bill.get_score(
												tensor_nonsmoker_total_bill).abs() > 3))
plt.xlabel('nonsmoker_total_bill')
plt.ylabel('nonsmoker_size')
plt.show()

"""Візуалізація Zscore для size серед курців"""
smoker_size_plot = sns.scatterplot(x=tensor_smoker_size, y=smoker_total_bill,
								   hue=(score_smoker_size.get_score(tensor_smoker_size).abs() > 3))
plt.xlabel('smoker_size')
plt.ylabel('smoker_total_bill')
plt.show()

"""Візуалізація Zscore для size серед некурців"""
nonsmoker_size_plot = sns.scatterplot(x=tensor_nonsmoker_size, y=nonsmoker_total_bill,
									  hue=(score_nonsmoker_size.get_score(tensor_nonsmoker_size).abs() > 3))
plt.xlabel('nonsmoker_size')
plt.ylabel('nonsmoker_total_bill')
plt.show()

"""Візуалізація Zscore для total_bill серед обіду"""
dinner_total_bill_plot = sns.scatterplot(x=tensor_dinner_total_bill, y=dinner_size,
										 hue=(score_dinner_total_bill.get_score(tensor_dinner_total_bill).abs() > 3))
plt.xlabel('dinner_total_bill')
plt.ylabel('dinner_size')
plt.show()

"""Візуалізація Zscore для total_bill серед ланчу"""
lunch_total_bill_plot = sns.scatterplot(x=tensor_lunch_total_bill, y=lunch_size,
										hue=(score_lunch_total_bill.get_score(
											tensor_lunch_total_bill).abs() > 3))
plt.xlabel('lunch_total_bill')
plt.ylabel('lunch_size')
plt.show()

"""Візуалізація Zscore для size серед обіду"""
dinner_size_plot = sns.scatterplot(x=tensor_dinner_size, y=dinner_total_bill,
								   hue=(score_dinner_size.get_score(tensor_dinner_size).abs() > 3))
plt.xlabel('dinner_size')
plt.ylabel('dinner_total_bill')
plt.show()

"""Візуалізація Zscore для size серед ланчу"""
lunch_size_plot = sns.scatterplot(x=tensor_lunch_size, y=lunch_total_bill,
								  hue=(score_lunch_size.get_score(tensor_lunch_size).abs() > 3))
plt.xlabel('lunch_size')
plt.ylabel('lunch_total_bill')
plt.show()
