import os
import time
from kaggle_downloader import kaggle_downloader

class Kernel:
    def __init__(self,  project_dir, notebooks_dir="notebooks", references_path="./references/kernels.txt"):
        self.notebooks_dir = notebooks_dir
        self.references_path = references_path
        self.references = self.load_references()
        self.delay = 5
        self.project_dir = project_dir
        self.downloader = kaggle_downloader(self.notebooks_dir)
        self.sortby = ['hotness', 'commentCount', 'dateCreated', 'dateRun', 'relevance', 'scoreAscending','scoreDescending', 'viewCount', 'voteCount']

    def load_references(self):
        if not os.path.exists(self.references_path):
            return []
        references = []
        with open(self.references_path, "r") as fid:
            for line in fid:
                references.append(line.strip())
        return references

    def add_references(self, new_references):
        counter = 0
        with open(self.references_path, "a") as fw:
            for ref in new_references:
                if ref not in self.references:
                    self.references.append(ref)
                    fw.write(ref + "\n")
                    counter = counter + 1
        print(f"Number of new kernels is {counter}")

    def download_list_of_kernels(self, sortid: int):
        pid = 0
        while True:
            pid = pid + 1
            responses = self.downloader.download_list_of_kernels(pid,self.sortby[sortid])
            if len(responses) == 0:
                break
            references = []
            for r in responses:
                references.append(vars(r)['ref'])
            time.sleep(self.delay)
            self.add_references(references)

    def download_list_of_kernels_by_dataset(self, dataset_ref: str):
        pid = 0
        while True:
            pid = pid + 1
            responses = self.downloader.download_list_of_kernels_by_dataset(pid,dataset_ref)
            if len(responses) == 0:
                break
            references = []
            for r in responses:
                references.append(vars(r)['ref'])
            time.sleep(self.delay)
            self.add_references(references)

    def download_list_of_kernels_by_user(self, user_ref: str):
        pid = 0
        while True:
            pid = pid + 1
            responses = self.downloader.download_list_of_kernels_by_user(pid,user_ref)
            references = []
            for r in responses:
                references.append(vars(r)['ref'])
            time.sleep(self.delay)
            self.add_references(references)
            if len(responses) < 90:
                break

    def download_kernels(self):
        kernels_num = len(self.references)
        counter = 1
        for ref in self.references:
            counter = counter + 1
            print(f"Download kernel number {counter} out of {kernels_num}")
            user, title = ref.split("/")
            if "exercise" in title:
                continue
            kernel_path = os.path.join(self.project_dir, self.notebooks_dir, user, title)
            if not os.path.isdir(kernel_path):
                self.downloader.download_kernel(ref)
                time.sleep(self.delay)
