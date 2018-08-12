"""最简单的想法：暴力求解"""


class Solution:
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		for i in range(len(nums)):
			for j in range(i + 1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i, j]


"""其实也是一个查找问题，
给其中一个数字，
然后查找另外一个数字是不是也在数组中，
由于字典的查找是比较快，
查找问题优先使用上字典"""


class Solution:
	def twoSum(self, nums, target):
		"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
		num = {}
		for i in range(len(nums)):
			num[nums[i]] = i
		# 如果nums中有相同的数，字典中对应的键值对是相同值的最后面的索引
		for i in range(len(nums)):
			if target - nums[i] in num:
				if num[target - nums[i]] != i:
					return [i, num[target - nums[i]]]


"""现在是我们自己定义了一个字典，
然后将给定的列表存进字典中，
python提供了内置函数enumerate() ，
用于将一个可遍历的数据对象(如列表，元组或字符串)组合为一个索引序列，
同时列出数据和数据下标，一般用在 for 循环当中"""


class Solution:
	def twoSum(self, nums, target):
		"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
		num = {}
		for i, element in enumerate(nums):
			if target - element in num:
				return [num[target - element], i]
			num[element] = i
