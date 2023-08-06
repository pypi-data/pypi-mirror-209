import setuptools

with open("VERSION", "r", encoding="utf8") as info:
    Version = info.readline().strip()

with open("README.md", "r", encoding="utf8") as desc:
    long_desc = ""
    for line in desc.readlines():
        if len(line) > 0 and '-' == line[0]:
            break
        else:
            long_desc += line

setuptools.setup(name="AIFloodMaster",
                 version=Version,
                 description="贵仁-智能雨洪管理模型",
                 long_description=long_desc,
                 long_description_content_type="text/markdown",
                 url="https://cloud.keepsoft.net/product",
                 include_package_data=True,
                 package_data={
                     "lstm_data": ["data/lstm-data/test-data/*.csv"],
                     "ddpg_data": [
                         "data/ddpg-swmm-data/obs_data_1month_all_controlled/*.inp",
                         "data/ddpg-swmm-data/obs_data_daily_fcsts/*.csv"
                     ]
                 },
                 packages=setuptools.find_packages(),
                 classifiers=["Programming Language :: Python :: 3.9"])
