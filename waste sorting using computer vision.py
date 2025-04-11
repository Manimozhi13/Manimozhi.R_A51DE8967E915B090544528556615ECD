{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMNacCD8lXpz25FtfJqFUlR",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Manimozhi13/Manimozhi.R_A51DE8967E915B090544528556615ECD/blob/main/waste%20sorting%20using%20computer%20vision.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 512
        },
        "id": "ax55ED7mDlQv",
        "outputId": "00f95697-022c-4971-b1d4-2a53d851e5c5"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "FileNotFoundError",
          "evalue": "[Errno 2] Unable to synchronously open file (unable to open file: name = 'waste_classifier_model.h5', errno = 2, error message = 'No such file or directory', flags = 0, o_flags = 0)",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-2-880502cbbb87>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;31m# Load your trained model\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0mmodel\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mload_model\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'waste_classifier_model.h5'\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# Replace with your model path\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;31m# Class names (change based on your model's training)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/keras/src/saving/saving_api.py\u001b[0m in \u001b[0;36mload_model\u001b[0;34m(filepath, custom_objects, compile, safe_mode)\u001b[0m\n\u001b[1;32m    194\u001b[0m         )\n\u001b[1;32m    195\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mendswith\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\".h5\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\".hdf5\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 196\u001b[0;31m         return legacy_h5_format.load_model_from_hdf5(\n\u001b[0m\u001b[1;32m    197\u001b[0m             \u001b[0mfilepath\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcustom_objects\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcustom_objects\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcompile\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcompile\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    198\u001b[0m         )\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/keras/src/legacy/saving/legacy_h5_format.py\u001b[0m in \u001b[0;36mload_model_from_hdf5\u001b[0;34m(filepath, custom_objects, compile)\u001b[0m\n\u001b[1;32m    114\u001b[0m     \u001b[0mopened_new_file\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mh5py\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mFile\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    115\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mopened_new_file\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 116\u001b[0;31m         \u001b[0mf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mh5py\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mFile\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmode\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"r\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    117\u001b[0m     \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    118\u001b[0m         \u001b[0mf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfilepath\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/h5py/_hl/files.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, name, mode, driver, libver, userblock_size, swmr, rdcc_nslots, rdcc_nbytes, rdcc_w0, track_order, fs_strategy, fs_persist, fs_threshold, fs_page_size, page_buf_size, min_meta_keep, min_raw_keep, locking, alignment_threshold, alignment_interval, meta_block_size, **kwds)\u001b[0m\n\u001b[1;32m    562\u001b[0m                                  \u001b[0mfs_persist\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mfs_persist\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfs_threshold\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mfs_threshold\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    563\u001b[0m                                  fs_page_size=fs_page_size)\n\u001b[0;32m--> 564\u001b[0;31m                 \u001b[0mfid\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmake_fid\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmode\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muserblock_size\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfapl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfcpl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mswmr\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mswmr\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    565\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    566\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlibver\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtuple\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/h5py/_hl/files.py\u001b[0m in \u001b[0;36mmake_fid\u001b[0;34m(name, mode, userblock_size, fapl, fcpl, swmr)\u001b[0m\n\u001b[1;32m    236\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mswmr\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mswmr_support\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    237\u001b[0m             \u001b[0mflags\u001b[0m \u001b[0;34m|=\u001b[0m \u001b[0mh5f\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mACC_SWMR_READ\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 238\u001b[0;31m         \u001b[0mfid\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mh5f\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mflags\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfapl\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mfapl\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    239\u001b[0m     \u001b[0;32melif\u001b[0m \u001b[0mmode\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'r+'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    240\u001b[0m         \u001b[0mfid\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mh5f\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mh5f\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mACC_RDWR\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfapl\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mfapl\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32mh5py/_objects.pyx\u001b[0m in \u001b[0;36mh5py._objects.with_phil.wrapper\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mh5py/_objects.pyx\u001b[0m in \u001b[0;36mh5py._objects.with_phil.wrapper\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mh5py/h5f.pyx\u001b[0m in \u001b[0;36mh5py.h5f.open\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] Unable to synchronously open file (unable to open file: name = 'waste_classifier_model.h5', errno = 2, error message = 'No such file or directory', flags = 0, o_flags = 0)"
          ]
        }
      ],
      "source": [
        "import cv2\n",
        "import numpy as np\n",
        "from tensorflow.keras.models import load_model\n",
        "\n",
        "# Load your trained model\n",
        "model = load_model('waste_classifier_model.h5')  # Replace with your model path\n",
        "\n",
        "# Class names (change based on your model's training)\n",
        "classes = ['Organic', 'Recyclable', 'Other']\n",
        "\n",
        "def preprocess_image(image_path):\n",
        "    img = cv2.imread(image_path)\n",
        "    img = cv2.resize(img, (224, 224))  # Resize as per model input\n",
        "    img = img / 255.0  # Normalize\n",
        "    img = np.expand_dims(img, axis=0)\n",
        "    return img\n",
        "\n",
        "def classify_waste(image_path):\n",
        "    img = preprocess_image(image_path)\n",
        "    prediction = model.predict(img)\n",
        "    class_index = np.argmax(prediction)\n",
        "    print(f\"Predicted Waste Type: {classes[class_index]}\")\n",
        "\n",
        "# Test with a sample image\n",
        "classify_waste('test_waste_image.jpg')  # Replace with your image path\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "h5V-0m-AECfm"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}