# from sklearn.metrics.pairwise import rbf_kernel
# from sklearn.linear_model import Ridge
# import matplotlib.pyplot as plt
# import numpy as np

# heights = np.asarray([1.32, 1.45, 1.66, 1.88]).reshape(-1, 1)
# weights = np.asarray([55, 67, 70, 100]).reshape(-1, 1)
# centers = np.asarray([1.0, 1.2, 1.4, 1.6, 1.8, 2.0]).reshape(-1, 1)
# print("centers.shape", centers.shape)
# print("heights.shape", heights.shape)
# print("weights.shape", weights.shape)

# # I recommend playing around with these parameters and seeing how well you fit
# # the data.  Changing one of the parameters will change the optimal value of
# # the other:
# sigma = 0.5 # actually alpha, width of the RBF
# alpha = 0.0001 # actually lambda, regularization

# # New representation:
# x = rbf_kernel(heights, centers, gamma=1 / sigma)
# print("x.shape", x.shape)
# print("Original inputs", heights)
# print("RBF repr", x)

# # Now go and fit a linear model between x and height
# regr = Ridge(alpha=alpha, fit_intercept=False)
# regr.fit(x, weights)
# print("Score on training data = ", regr.score(x, weights))
# all_x = np.linspace(-3.0, 5.0, 1000).reshape(-1, 1)

# # New representation:
# expanded_x = rbf_kernel(all_x, centers, gamma=1 / sigma)
# all_y = regr.predict(expanded_x)
# print("all_x.shape", all_x.shape)
# print("expanded_x.shape", expanded_x.shape)
# print("all_y.shape", all_y.shape)

# # Show that the predictions tend to zero far away from inputs
# plt.figure()
# plt.plot(all_x, all_y)
# plt.scatter(heights, weights)

# # Zoom in and see how well predictions fit the data
# zoom_ind = (all_x > heights.min()) & (all_x < heights.max())
# plt.figure()
# plt.plot(all_x[zoom_ind], all_y[zoom_ind])
# plt.scatter(heights, weights)
# plt.show()

