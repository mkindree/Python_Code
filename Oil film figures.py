#%% Oil film stuff



for g in [0, 1]:
    plt.figure()
    ax1 = plt.subplot(3, 3, 1, aspect='equal')
    plt.pcolormesh(x_g[g][:, :, 0], y_g[g][:, :, 0], M_dU_dx_g[g][:, :, 0])
    plt.title(r'$\displaystyle \frac{d\overline{U}}{dx}$')
    ax2 = plt.subplot(3, 3, 2, aspect='equal')
    plt.pcolormesh(x_g[g][:, :, 0], y_g[g][:, :, 0], M_dV_dx_g[g][:, :, 0])
    plt.title(r'$\displaystyle \frac{d\overline{V}}{dx}$')
    ax3 = plt.subplot(3, 3, 3, aspect='equal')
    plt.pcolormesh(x_g[g][:, :, 0], y_g[g][:, :, 0], M_dW_dx_g[g][:, :, 0])
    plt.title(r'$\displaystyle \frac{d\overline{W}}{dx}$')
    ax4 = plt.subplot(3, 3, 4, aspect='equal')
    plt.pcolormesh(x_g[g][:, :, 0], y_g[g][:, :, 0], M_dU_dy_g[g][:, :, 0])
    plt.title(r'$\displaystyle \frac{d\overline{U}}{dy}$')
    ax5 = plt.subplot(3, 3, 5, aspect='equal')
    plt.pcolormesh(x_g[g][:, :, 0], y_g[g][:, :, 0], M_dV_dy_g[g][:, :, 0])
    plt.title(r'$\displaystyle \frac{d\overline{V}}{dy}$')
    ax6 = plt.subplot(3, 3, 6, aspect='equal')
    plt.pcolormesh(x_g[g][:, :, 0], y_g[g][:, :, 0], M_dW_dy_g[g][:, :, 0])
    plt.title(r'$\displaystyle \frac{d\overline{W}}{dy}$')
    ax7 = plt.subplot(3, 3, 7, aspect='equal')
    plt.pcolormesh(x_g[g][:, :, 0], y_g[g][:, :, 0], M_dU_dz_g[g][:, :, 0])
    plt.title(r'$\displaystyle \frac{d\overline{U}}{dz}$')
    ax8 = plt.subplot(3, 3, 8, aspect='equal')
    plt.pcolormesh(x_g[g][:, :, 0], y_g[g][:, :, 0], M_dV_dz_g[g][:, :, 0])
    plt.title(r'$\displaystyle \frac{d\overline{V}}{dz}$')
    ax9 = plt.subplot(3, 3, 9, aspect='equal')
    plt.pcolormesh(x_g[g][:, :, 0], y_g[g][:, :, 0], M_dW_dz_g[g][:, :, 0])
    plt.title(r'$\displaystyle \frac{d\overline{W}}{dz}$')
    
    plt.figure()
    ax1 = plt.subplot(3, 3, 1, aspect='equal')
    plt.pcolormesh(x_g[g][:, :, 0], y_g[g][:, :, 0], 2*M_dU_dx_g[g][:, :, 0])
    plt.title(r'$\displaystyle \overline{\tau_{xx}}$')
    ax2 = plt.subplot(3, 3, 2, aspect='equal')
    plt.pcolormesh(x_g[g][:,:, 0], y_g[g][:, :, 0], 2*M_dV_dy_g[g][:, :, 0])
    plt.title(r'$\displaystyle \overline{\tau_{yy}}$')
    ax3 = plt.subplot(3, 3, 3, aspect='equal')
    plt.pcolormesh(x_g[g][:, :, 0], y_g[g][:, :, 0], 2*M_dW_dz_g[g][:, :, 0])
    plt.title(r'$\displaystyle \overline{\tau_{zz}}$')
    ax4 = plt.subplot(3, 3, 4, aspect='equal')
    plt.pcolormesh(x_g[g][:, :, 0], y_g[g][:, :, 0], M_dU_dy_g[g][:, :, 0] + M_dV_dx_g[g][:, :, 0])
    plt.title(r'$\displaystyle \overline{\tau_{xy}}$')
    ax5 = plt.subplot(3, 3, 5, aspect='equal')
    plt.pcolormesh(x_g[g][:, :, 0], y_g[g][:, :, 0], M_dU_dz_g[g][:, :, 0] + M_dW_dx_g[g][:, :, 0])
    plt.title(r'$\displaystyle \overline{\tau_{yz}}$')
    ax6 = plt.subplot(3, 3, 6, aspect='equal')
    plt.pcolormesh(x_g[g][:, :, 0], y_g[g][:, :, 0], M_dV_dz_g[g][:, :, 0] + M_dW_dy_g[g][:, :, 0])
    plt.title(r'$\displaystyle \overline{\tau_{xz}}$')