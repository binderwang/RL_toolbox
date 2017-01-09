import tensorflow as tf

# class PMS_base(object):
#     flags = tf.app.flags
#     flags.DEFINE_integer('obs_height', 100, 'image height')
#     flags.DEFINE_integer('obs_width', 100, 'image width')
#     flags.DEFINE_integer('obs_channel', 3, 'image channel')
#     flags.DEFINE_integer('history_number', 2, 'image history number')
#     flags.DEFINE_integer('jobs', 4, 'thread or process number')
#     flags.DEFINE_integer('max_iter_number', 400, 'control the max iteration number for trainning')
#     flags.DEFINE_integer('paths_number', 10, 'number of paths in each rollout')
#     flags.DEFINE_integer('max_path_length',200, 'timesteps in each path')
#     flags.DEFINE_integer('batch_size', 100, 'batch size for trainning')
#     flags.DEFINE_float('max_kl', 0.01, 'the largest kl distance, \sigma in paper')
#     flags.DEFINE_float('gae_lambda', 1.0, 'fix number')
#     flags.DEFINE_float('subsample_factor', 0.5, 'ratio of the samples used in training process')
#     flags.DEFINE_float('cg_damping', 0.001, 'conjugate gradient damping')
#     flags.DEFINE_float('discount', 0.99, 'discount')
#     flags.DEFINE_integer('cg_iters', 20, 'iteration number in conjugate gradient')
#     flags.DEFINE_float('deviation', 0.1, 'fixed')
#     flags.DEFINE_boolean('render', False, 'whether to render image')
#     flags.DEFINE_boolean('train_flag', True, 'true for train and False for test')
#     flags.DEFINE_integer('iter_num_per_train', 1, 'iteration number in each trainning process')
#     flags.DEFINE_string('checkpoint_file', '', 'checkpoint file path, if empty then will load the latest one')
#     flags.DEFINE_integer('save_model_times', 1, 'iteration number to save model, if 1, then model would be saved in each iteration')
#     flags.DEFINE_boolean('record_movie', False, 'whether record the video in gym')
#     flags.DEFINE_boolean('upload_to_gym', False, 'whether upload the result to gym')
#     flags.DEFINE_string('checkpoint_dir', 'checkpoint/', 'checkpoint save and load path, for parallel, it should be checkpoint_parallel')
#     flags.DEFINE_string('environment_name', 'Pendulum-v0', 'environment name')
#     flags.DEFINE_float('min_std', 0.2, 'the smallest std')
#     flags.DEFINE_boolean('center_adv', True, 'whether center advantage, fixed')
#     flags.DEFINE_boolean('positive_adv', False, 'whether positive advantage, fixed')
#     flags.DEFINE_boolean('use_std_network', False, 'whether use network to train std, it is not supported, fixed')
#     flags.DEFINE_float('std', 1.1, 'if the std is set to constant, then this value will be used')
#     flags.DEFINE_integer('obs_shape', 3, 'dimensions of observation')
#     flags.DEFINE_integer('action_shape', 1, 'dimensions of action')
#     flags.DEFINE_float('min_a', -2.0, 'the smallest action value')
#     flags.DEFINE_float('max_a', 2.0, 'the largest action value')
#     flags.DEFINE_string("decay_method", "adaptive", "decay_method:adaptive, linear, exponential") # adaptive, linear, exponential
#     flags.DEFINE_integer("timestep_adapt", 600, "timestep to adapt kl")
#     flags.DEFINE_float("kl_adapt", 0.0005, "kl adapt rate")
#     pms = flags.FLAGS
#     pms.checkpoint_file = None
#     pms.batch_size = int(pms.subsample_factor * pms.paths_number * pms.max_path_length)

class PMS_dqn(object):
    flags = tf.app.flags
    flags.DEFINE_integer('obs_height', 100, 'image height')
    flags.DEFINE_integer('obs_width', 100, 'image width')
    flags.DEFINE_integer('obs_channel', 3, 'image channel')
    flags.DEFINE_integer('history_number', 2, 'image history number')
    flags.DEFINE_integer('jobs', 4, 'thread or process number')
    flags.DEFINE_integer('max_iter_number', 400, 'control the max iteration number for trainning')
    flags.DEFINE_integer('paths_number', 10, 'number of paths in each rollout')
    flags.DEFINE_integer('max_path_length', 200, 'timesteps in each path')
    flags.DEFINE_integer('batch_size', 100, 'batch size for trainning')
    flags.DEFINE_float('subsample_factor', 0.5, 'ratio of the samples used in training process')
    flags.DEFINE_float('cg_damping', 0.001, 'conjugate gradient damping')
    flags.DEFINE_float('discount', 0.99, 'discount')
    flags.DEFINE_float('deviation', 0.1, 'fixed')
    flags.DEFINE_boolean('render', False, 'whether to render image')
    flags.DEFINE_boolean('train_flag', True, 'true for train and False for test')
    flags.DEFINE_integer('iter_num_per_train', 1, 'iteration number in each trainning process')
    flags.DEFINE_string('checkpoint_file', '', 'checkpoint file path, if empty then will load the latest one')
    flags.DEFINE_integer('save_model_times', 1,
                         'iteration number to save model, if 1, then model would be saved in each iteration')
    flags.DEFINE_boolean('record_movie', False, 'whether record the video in gym')
    flags.DEFINE_boolean('upload_to_gym', False, 'whether upload the result to gym')
    flags.DEFINE_string('checkpoint_dir', 'checkpoint/',
                        'checkpoint save and load path, for parallel, it should be checkpoint_parallel')
    flags.DEFINE_string('environment_name', 'MountainCar-v0', 'environment name')
    flags.DEFINE_float('min_std', 0.2, 'the smallest std')
    flags.DEFINE_integer('obs_shape', 2, 'dimensions of observation')
    flags.DEFINE_integer('action_shape', 1, 'dimensions of action')
    flags.DEFINE_float('min_a', -2.0, 'the smallest action value')
    flags.DEFINE_float('max_a', 2.0, 'the largest action value')
    flags.DEFINE_string("decay_method", "adaptive",
                        "decay_method:adaptive, linear, exponential")  # adaptive, linear, exponential
    flags.DEFINE_integer("timestep_adapt", 600, "timestep to adapt kl")
    flags.DEFINE_integer("max_size", 10000, "timestep to adapt kl")
    flags.DEFINE_float('learning_rate_minimum', 0.002, 'learning_rate_minimum')
    flags.DEFINE_float('learning_rate', 0.002, 'learning_rate')
    flags.DEFINE_float('learning_rate_decay', 0.002, 'learning_rate_decay')
    flags.DEFINE_integer("learning_rate_decay_step", 100, "learning_rate_decay_step")

    pms = flags.FLAGS
    pms.checkpoint_file = None