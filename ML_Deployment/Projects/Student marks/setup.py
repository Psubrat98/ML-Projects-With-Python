{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPwWnbW4hA2lwgpdvbI/tO2"
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
      "cell_type": "code",
      "source": [
        "from setuptools import find_packages, setup"
      ],
      "metadata": {
        "id": "Q3_e5VxBNIPw"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "setup(\n",
        "    name='mlproject',\n",
        "    version='0.0.1',\n",
        "    author='Subrat',\n",
        "    author_email='psub44@gmail.com',\n",
        "    packages=find_packages(),\n",
        "    install_requires=[],\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "w6ARWJ3yOVng",
        "outputId": "3664a7a2-019c-4442-e613-fbee33186cb0"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "ERROR:root:Internal Python error in the inspect module.\n",
            "Below is the traceback from this internal error.\n",
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Traceback (most recent call last):\n",
            "  File \"/usr/lib/python3.9/distutils/fancy_getopt.py\", line 233, in getopt\n",
            "    opts, args = getopt.getopt(args, short_opts, self.long_opts)\n",
            "  File \"/usr/lib/python3.9/getopt.py\", line 95, in getopt\n",
            "    opts, args = do_shorts(opts, args[0][1:], shortopts, args[1:])\n",
            "  File \"/usr/lib/python3.9/getopt.py\", line 195, in do_shorts\n",
            "    if short_has_arg(opt, shortopts):\n",
            "  File \"/usr/lib/python3.9/getopt.py\", line 211, in short_has_arg\n",
            "    raise GetoptError(_('option -%s not recognized') % opt, opt)\n",
            "getopt.GetoptError: option -f not recognized\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/lib/python3.9/distutils/core.py\", line 134, in setup\n",
            "    ok = dist.parse_command_line()\n",
            "  File \"/usr/lib/python3.9/distutils/dist.py\", line 475, in parse_command_line\n",
            "    args = parser.getopt(args=self.script_args, object=self)\n",
            "  File \"/usr/lib/python3.9/distutils/fancy_getopt.py\", line 235, in getopt\n",
            "    raise DistutilsArgError(msg)\n",
            "distutils.errors.DistutilsArgError: option -f not recognized\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.9/dist-packages/IPython/core/interactiveshell.py\", line 3553, in run_code\n",
            "    exec(code_obj, self.user_global_ns, self.user_ns)\n",
            "  File \"<ipython-input-5-51b90e0aa908>\", line 1, in <cell line: 1>\n",
            "    setup(\n",
            "  File \"/usr/local/lib/python3.9/dist-packages/setuptools/__init__.py\", line 108, in setup\n",
            "    return distutils.core.setup(**attrs)\n",
            "  File \"/usr/lib/python3.9/distutils/core.py\", line 136, in setup\n",
            "    raise SystemExit(gen_usage(dist.script_name) + \"\\nerror: %s\" % msg)\n",
            "SystemExit: usage: ipykernel_launcher.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]\n",
            "   or: ipykernel_launcher.py --help [cmd1 cmd2 ...]\n",
            "   or: ipykernel_launcher.py --help-commands\n",
            "   or: ipykernel_launcher.py cmd --help\n",
            "\n",
            "error: option -f not recognized\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.9/dist-packages/IPython/core/ultratb.py\", line 1101, in get_records\n",
            "    return _fixed_getinnerframes(etb, number_of_lines_of_context, tb_offset)\n",
            "  File \"/usr/local/lib/python3.9/dist-packages/IPython/core/ultratb.py\", line 248, in wrapped\n",
            "    return f(*args, **kwargs)\n",
            "  File \"/usr/local/lib/python3.9/dist-packages/IPython/core/ultratb.py\", line 281, in _fixed_getinnerframes\n",
            "    records = fix_frame_records_filenames(inspect.getinnerframes(etb, context))\n",
            "  File \"/usr/lib/python3.9/inspect.py\", line 1543, in getinnerframes\n",
            "    frameinfo = (tb.tb_frame,) + getframeinfo(tb, context)\n",
            "AttributeError: 'tuple' object has no attribute 'tb_frame'\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mGetoptError\u001b[0m                               Traceback (most recent call last)",
            "\u001b[0;32m/usr/lib/python3.9/distutils/fancy_getopt.py\u001b[0m in \u001b[0;36mgetopt\u001b[0;34m(self, args, object)\u001b[0m\n\u001b[1;32m    232\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 233\u001b[0;31m             \u001b[0mopts\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0margs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgetopt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgetopt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mshort_opts\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlong_opts\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    234\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mgetopt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.9/getopt.py\u001b[0m in \u001b[0;36mgetopt\u001b[0;34m(args, shortopts, longopts)\u001b[0m\n\u001b[1;32m     94\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 95\u001b[0;31m             \u001b[0mopts\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0margs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdo_shorts\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mopts\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0margs\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mshortopts\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0margs\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     96\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.9/getopt.py\u001b[0m in \u001b[0;36mdo_shorts\u001b[0;34m(opts, optstring, shortopts, args)\u001b[0m\n\u001b[1;32m    194\u001b[0m         \u001b[0mopt\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptstring\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moptstring\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptstring\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 195\u001b[0;31m         \u001b[0;32mif\u001b[0m \u001b[0mshort_has_arg\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mopt\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mshortopts\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    196\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0moptstring\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m''\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.9/getopt.py\u001b[0m in \u001b[0;36mshort_has_arg\u001b[0;34m(opt, shortopts)\u001b[0m\n\u001b[1;32m    210\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mshortopts\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstartswith\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m':'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 211\u001b[0;31m     \u001b[0;32mraise\u001b[0m \u001b[0mGetoptError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m_\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'option -%s not recognized'\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0mopt\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mopt\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    212\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mGetoptError\u001b[0m: option -f not recognized",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mDistutilsArgError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/usr/lib/python3.9/distutils/core.py\u001b[0m in \u001b[0;36msetup\u001b[0;34m(**attrs)\u001b[0m\n\u001b[1;32m    133\u001b[0m     \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 134\u001b[0;31m         \u001b[0mok\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdist\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mparse_command_line\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    135\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0mDistutilsArgError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.9/distutils/dist.py\u001b[0m in \u001b[0;36mparse_command_line\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    474\u001b[0m         \u001b[0mparser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mset_aliases\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m{\u001b[0m\u001b[0;34m'licence'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m'license'\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 475\u001b[0;31m         \u001b[0margs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mparser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgetopt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscript_args\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mobject\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    476\u001b[0m         \u001b[0moption_order\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mparser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_option_order\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.9/distutils/fancy_getopt.py\u001b[0m in \u001b[0;36mgetopt\u001b[0;34m(self, args, object)\u001b[0m\n\u001b[1;32m    234\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mgetopt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 235\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mDistutilsArgError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    236\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mDistutilsArgError\u001b[0m: option -f not recognized",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mSystemExit\u001b[0m                                Traceback (most recent call last)",
            "    \u001b[0;31m[... skipping hidden 1 frame]\u001b[0m\n",
            "\u001b[0;32m<ipython-input-5-51b90e0aa908>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m setup(\n\u001b[0m\u001b[1;32m      2\u001b[0m     \u001b[0mname\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'mlproject'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m     \u001b[0mversion\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'0.0.1'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/setuptools/__init__.py\u001b[0m in \u001b[0;36msetup\u001b[0;34m(**attrs)\u001b[0m\n\u001b[1;32m    107\u001b[0m     \u001b[0m_install_setup_requires\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mattrs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 108\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0mdistutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcore\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msetup\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m**\u001b[0m\u001b[0mattrs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    109\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.9/distutils/core.py\u001b[0m in \u001b[0;36msetup\u001b[0;34m(**attrs)\u001b[0m\n\u001b[1;32m    135\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0mDistutilsArgError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 136\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mSystemExit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mgen_usage\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdist\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscript_name\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;34m\"\\nerror: %s\"\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    137\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mSystemExit\u001b[0m: usage: ipykernel_launcher.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]\n   or: ipykernel_launcher.py --help [cmd1 cmd2 ...]\n   or: ipykernel_launcher.py --help-commands\n   or: ipykernel_launcher.py cmd --help\n\nerror: option -f not recognized",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "    \u001b[0;31m[... skipping hidden 1 frame]\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/IPython/core/interactiveshell.py\u001b[0m in \u001b[0;36mshowtraceback\u001b[0;34m(self, exc_tuple, filename, tb_offset, exception_only, running_compiled_code)\u001b[0m\n\u001b[1;32m   2090\u001b[0m                     stb = ['An exception has occurred, use %tb to see '\n\u001b[1;32m   2091\u001b[0m                            'the full traceback.\\n']\n\u001b[0;32m-> 2092\u001b[0;31m                     stb.extend(self.InteractiveTB.get_exception_only(etype,\n\u001b[0m\u001b[1;32m   2093\u001b[0m                                                                      value))\n\u001b[1;32m   2094\u001b[0m                 \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/IPython/core/ultratb.py\u001b[0m in \u001b[0;36mget_exception_only\u001b[0;34m(self, etype, value)\u001b[0m\n\u001b[1;32m    752\u001b[0m         \u001b[0mvalue\u001b[0m \u001b[0;34m:\u001b[0m \u001b[0mexception\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    753\u001b[0m         \"\"\"\n\u001b[0;32m--> 754\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mListTB\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstructured_traceback\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0metype\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    755\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    756\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mshow_exception_only\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0metype\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mevalue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/IPython/core/ultratb.py\u001b[0m in \u001b[0;36mstructured_traceback\u001b[0;34m(self, etype, evalue, etb, tb_offset, context)\u001b[0m\n\u001b[1;32m    627\u001b[0m             \u001b[0mchained_exceptions_tb_offset\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    628\u001b[0m             out_list = (\n\u001b[0;32m--> 629\u001b[0;31m                 self.structured_traceback(\n\u001b[0m\u001b[1;32m    630\u001b[0m                     \u001b[0metype\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mevalue\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0metb\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mchained_exc_ids\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    631\u001b[0m                     chained_exceptions_tb_offset, context)\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/IPython/core/ultratb.py\u001b[0m in \u001b[0;36mstructured_traceback\u001b[0;34m(self, etype, value, tb, tb_offset, number_of_lines_of_context)\u001b[0m\n\u001b[1;32m   1365\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1366\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtb\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtb\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1367\u001b[0;31m         return FormattedTB.structured_traceback(\n\u001b[0m\u001b[1;32m   1368\u001b[0m             self, etype, value, tb, tb_offset, number_of_lines_of_context)\n\u001b[1;32m   1369\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/IPython/core/ultratb.py\u001b[0m in \u001b[0;36mstructured_traceback\u001b[0;34m(self, etype, value, tb, tb_offset, number_of_lines_of_context)\u001b[0m\n\u001b[1;32m   1265\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mmode\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mverbose_modes\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1266\u001b[0m             \u001b[0;31m# Verbose modes need a full traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1267\u001b[0;31m             return VerboseTB.structured_traceback(\n\u001b[0m\u001b[1;32m   1268\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0metype\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtb\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtb_offset\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnumber_of_lines_of_context\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1269\u001b[0m             )\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/IPython/core/ultratb.py\u001b[0m in \u001b[0;36mstructured_traceback\u001b[0;34m(self, etype, evalue, etb, tb_offset, number_of_lines_of_context)\u001b[0m\n\u001b[1;32m   1122\u001b[0m         \u001b[0;34m\"\"\"Return a nice text document describing the traceback.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1123\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1124\u001b[0;31m         formatted_exception = self.format_exception_as_a_whole(etype, evalue, etb, number_of_lines_of_context,\n\u001b[0m\u001b[1;32m   1125\u001b[0m                                                                tb_offset)\n\u001b[1;32m   1126\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/IPython/core/ultratb.py\u001b[0m in \u001b[0;36mformat_exception_as_a_whole\u001b[0;34m(self, etype, evalue, etb, number_of_lines_of_context, tb_offset)\u001b[0m\n\u001b[1;32m   1080\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1081\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1082\u001b[0;31m         \u001b[0mlast_unique\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrecursion_repeat\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfind_recursion\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0morig_etype\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mevalue\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrecords\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1083\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1084\u001b[0m         \u001b[0mframes\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat_records\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrecords\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlast_unique\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrecursion_repeat\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/IPython/core/ultratb.py\u001b[0m in \u001b[0;36mfind_recursion\u001b[0;34m(etype, value, records)\u001b[0m\n\u001b[1;32m    380\u001b[0m     \u001b[0;31m# first frame (from in to out) that looks different.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    381\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mis_recursion_error\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0metype\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrecords\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 382\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrecords\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    383\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    384\u001b[0m     \u001b[0;31m# Select filename, lineno, func_name to track frames with\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: object of type 'NoneType' has no len()"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "i09MK82FPH87"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}