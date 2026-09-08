import matplotlib.pyplot as plt


def plot_bbs_improvement(data, save_path):

    plt.figure(figsize=(8, 5))

    plt.plot(
        data["patient_id"],
        data["BBS_before"],
        marker="o",
        label="Before"
    )

    plt.plot(
        data["patient_id"],
        data["BBS_after"],
        marker="o",
        label="After"
    )

    plt.title("BBS Improvement After Rehabilitation")
    plt.xlabel("Patient")
    plt.ylabel("BBS Score")
    plt.legend()

    plt.savefig(save_path, bbox_inches="tight")
    plt.close()