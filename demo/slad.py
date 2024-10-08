
dataset_info = dict(
    dataset_name='slad',
    paper_info=dict(
        author='Zhang, Mingxin and Zhang, Qian and Song, Ran and Rosin, Paul L. and Zhang, Wei',
        title='Ship Landmark: An Informative Ship Image Annotation and Its Applications',
        container='IEEE Transactions on Intelligent Transportation Systems',
        year='2024',
        homepage='https://vsislab.github.io/Ships_VSIS/',
    ),
    keypoint_info={
         0 : 
        dict(
            name='right_side_forecastle_deck',
            id=0,
            color=[242, 12, 12],
            type='upper',
            swap='left_side_forecastle_deck' ),
         1 : 
        dict(
            name='left_side_forecastle_deck',
            id=1,
            color=[242, 70, 12],
            type='upper',
            swap='right_side_forecastle_deck' ),
         2 : 
        dict(
            name='bow_peak',
            id=2,
            color=[242, 127, 12],
            type='upper',
            swap='' ),
         3 : 
        dict(
            name='bow_inflexion',
            id=3,
            color=[255, 255, 255],
            type='lower',
            swap='' ),
         4 : 
        dict(
            name='vice_bow_peak',
            id=4,
            color=[255, 255, 255],
            type='lower',
            swap='' ),
         5 : 
        dict(
            name='bow_waterline',
            id=5,
            color=[255, 255, 255],
            type='lower',
            swap='' ),
         6 : 
        dict(
            name='right_stern_waterline',
            id=6,
            color=[255, 255, 255],
            type='lower',
            swap='left_stern_waterline' ),
         7 : 
        dict(
            name='left_stern_waterline',
            id=7,
            color=[255, 255, 255],
            type='lower',
            swap='right_stern_waterline' ),
         8 : 
        dict(
            name='right_stern_inflexion',
            id=8,
            color=[255, 255, 255],
            type='lower',
            swap='left_stern_inflexion' ),
         9 : 
        dict(
            name='left_stern_inflexion',
            id=9,
            color=[255, 255, 255],
            type='lower',
            swap='right_stern_inflexion' ),
         10 : 
        dict(
            name='right_stern_peak',
            id=10,
            color=[12, 242, 127],
            type='upper',
            swap='left_stern_peak' ),
         11 : 
        dict(
            name='left_stern_peak',
            id=11,
            color=[12, 242, 184],
            type='upper',
            swap='right_stern_peak' ),
         12 : 
        dict(
             name='right_deck_house_bottom_back',
            id=12,
            color=[255, 255, 255],
            type='upper',
            swap='left_deck_house_bottom_back' ),
         13 : 
        dict(
            name='left_deck_house_bottom_back',
            id=13,
            color=[255, 255, 255],
            type='upper',
            swap='right_deck_house_bottom_back' ),
         14 : 
        dict(
            name='right_deck_house_top_back',
            id=14,
            color=[12, 127, 242],
            type='upper',
            swap='left_deck_house_top_back' ),
         15 : 
        dict(
            name='left_deck_house_top_back',
            id=15,
            color=[12, 70, 242],
            type='upper',
            swap='right_deck_house_top_back' ),
         16 : 
        dict(
            name='right_deck_house_top_front',
            id=16,
            color=[12, 12, 242],
            type='upper',
            swap='left_deck_house_top_front' ),
         17 : 
        dict(
            name='left_deck_house_top_front',
            id=17,
            color=[70, 12, 242],
            type='upper',
            swap='right_deck_house_top_front' ),
         18 : 
        dict(
            name='right_deck_house_bottom_front',
            id=18,
            color=[255, 255, 255],
            type='upper',
            swap='left_deck_house_bottom_front' ),
         19 : 
        dict(
            name='left_deck_house_bottom_front',
            id=19,
            color=[255, 255, 255],
            type='upper',
            swap='right_deck_house_bottom_front' )
    },
    skeleton_info={
        0:
        dict(link=('right_side_forecastle_deck', 'bow_peak'), id=0, color=[253, 22, 22]),
        1:
        dict(link=('left_side_forecastle_deck', 'bow_peak'), id=1, color=[245, 59, 16]),
        2:
        dict(link=('right_side_forecastle_deck', 'left_side_forecastle_deck'), id=2, color=[254, 102, 11]),
        3:
        dict(link=('bow_peak', 'bow_inflexion'), id=3, color=[244, 152, 32]),
        4:
        dict(link=('right_stern_peak', 'left_stern_peak'), id=4, color=[252, 192, 13]),
        5:
        dict(link=('right_stern_peak', 'right_side_forecastle_deck'), id=5, color=[249, 234, 10]),
        6:
        dict(link=('left_stern_peak', 'left_side_forecastle_deck'), id=6, color=[223, 247, 53]),
        7:
        dict(link=('right_stern_peak', 'right_deck_house_top_back'), id=7, color=[180, 251, 26]),
        8:
        dict(link=('left_stern_peak', 'left_deck_house_top_back'), id=8, color=[146, 252, 40]),
        9:
        dict(link=('right_deck_house_top_back', 'left_deck_house_top_back'), id=9, color=[85, 249, 11]),
        10:
        dict(link=('right_deck_house_top_back', 'right_deck_house_top_front'), id=10, color=[45, 254, 15]),
        11:
        dict(link=('left_deck_house_top_back', 'left_deck_house_top_front'), id=11, color=[40, 249, 53]),
        12:
        dict(link=('right_deck_house_top_front', 'left_deck_house_top_front'), id=12, color=[48, 249, 99]),
        13:
        dict(link=('right_deck_house_top_front', 'right_side_forecastle_deck'), id=13, color=[28, 243, 122]),
        14:
        dict(link=('left_deck_house_top_front', 'left_side_forecastle_deck'), id=14, color=[23, 248, 164])

    },
    joint_weights=[
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1.
    ],
    sigmas=[0.041, 0.068, 0.053, 0.020, 0.013, 0.055, 0.020, \
                                               0.049, 0.023, 0.020, 0.023, 0.040, 0.026, 0.027, 0.040, 0.046, 0.040, 0.072, 0.028, 0.032]
   )
