import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # dataset_name = "monks-1"
    dataset_name = "adult"
    random_idx = 1
    workspace = "new_files_parallel_new"
    fig, axs = plt.subplots(nrows=1, ncols=2, sharey=False, figsize=(15, 5))
    ax2s = []
    f_data, u_data = [], []
    f_consts, u_consts = [], []
    for tmpi, n in enumerate([5, 10, 20]):
        # constr_val = 0.1
        # tmp_data = np.load(f"{workspace}/obj_{dataset_name}_{n}_{random_idx}.npy")
        # tmp_consts = np.load(f"{workspace}/constr_{dataset_name}_{n}_{random_idx}.npy")

        import json
        tmp_my_dict = open(f"{workspace}/{dataset_name}_repeat_{n}_{random_idx}.json")
        tmp_my_dict = json.load(tmp_my_dict)
        tmp_data = tmp_my_dict[str(n)][str(random_idx)]['u_obj']
        tmp_consts = tmp_my_dict[str(n)][str(random_idx)]['u_constr']

        f_data.append(tmp_data)
        f_consts.append(tmp_consts)
        
        tmp_my_dict = open(f"{workspace}/{dataset_name}_repeat_{n}_{random_idx}.json")
        tmp_my_dict = json.load(tmp_my_dict)
        tmp_data = tmp_my_dict[str(n)][str(random_idx)]['f_obj']
        tmp_consts = tmp_my_dict[str(n)][str(random_idx)]['f_constr']
        

        u_data.append(tmp_data)
        u_consts.append(tmp_consts)
   

    import matplotlib.pyplot as plt
        
    labels = ["5", "10", "20"]
    ax = axs[1]
    bplot1_1 = ax.boxplot(f_consts,
            vert=True,  # vertical box alignment
            patch_artist=True,  # fill with color
            showfliers=False,
            positions=np.array(np.arange(len(f_consts)))*2.0-0.35)
    bplot1 = ax.boxplot(u_consts,
            vert=True,  # vertical box alignment
            patch_artist=True,  # fill with color
            showfliers=False,
            positions=np.array(np.arange(len(f_consts)))*2.0+0.35)
    
    


    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # ax.set_ylabel('iterations', color="tab:blue", fontsize=15)
    ax.tick_params(axis='y')
    
    
    
    
    ax2 = axs[0]
    # ax2.set_yscale('log')
    
    bplot2_2 = ax2.boxplot(f_data,
                vert=True,  # vertical box alignment
                patch_artist=True,  # fill with color
                showfliers=False,
                positions=np.array(np.arange(len(f_data)))*2.0-0.35)
    
    bplot2 = ax2.boxplot(u_data,
            vert=True,  # vertical box alignment
            patch_artist=True,  # fill with color
            showfliers=False,
            positions=np.array(np.arange(len(f_data)))*2.0+0.35)
    
    ax2.tick_params(axis='y')
    ax2.spines['top'].set_visible(False)
    
    ax.set_xlabel('number of clients', fontsize=15)
    ax2.set_xlabel('number of clients', fontsize=15)
    
    

    # ax.set_title(f"loss disparity", fontsize=15)
    # ax2.set_title(f"classification loss", fontsize=15)
    
    # colors = ['pink', 'lightblue', 'lightgreen']
    # for bplot in (bplot1, bplot2, bplot1_1, bplot2_2):
    #     for patch, color in zip(bplot['boxes'], colors):
    #         patch.set_facecolor(color)
    
    # by iterating over all properties of the box plot
    def define_box_properties(plot_name, color_code, label, tmp_ax=None):
        # for k, v in plot_name.items():
            # plt.setp(plot_name.get(k), color=color_code)
        for patch in plot_name['boxes']:
            patch.set_facecolor(color_code)
        
            
        # use plot function to draw a small line to name the legend.
        tmp_ax.plot([], c=color_code, label=label)
        # tmp_ax.legend(loc="best")
        
    define_box_properties(bplot1, "tab:blue", "constrained model", ax)
    define_box_properties(bplot1_1, "brown", "unconstrained model", ax)
    define_box_properties(bplot2, "tab:blue", "constrained model", ax2)
    define_box_properties(bplot2_2, "brown", "unconstrained model", ax2)

    # for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
    for element in ['whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(bplot1[element], color="black")
        plt.setp(bplot1_1[element], color="black")
        plt.setp(bplot2[element], color="black")
        plt.setp(bplot2_2[element], color="black")
        

    ax.axhline(0.1, linestyle="--",c='black', alpha=0.8)
    leg1 = ax.legend(loc="best", fontsize=12)
    leg2 = ax2.legend(loc="best", fontsize=12)
    
    for line in leg1.get_lines():
        line.set_linewidth(6.0)
    for line in leg2.get_lines():
        line.set_linewidth(6.0)
    
    ax.set_xticks(np.arange(0, len(labels) * 2, 2), labels)
    ax2.set_xticks(np.arange(0, len(labels) * 2, 2), labels)
    ax.set_ylabel("loss disparity", fontsize=15)
    ax2.set_ylabel('objective value', fontsize=15)
    # plt.title("adult-b")
    fig.suptitle('adult-b', fontsize=15)
    
    
    plt.savefig(f"test.png", bbox_inches = 'tight')