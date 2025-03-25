import kaggle

class kaggle_downloader:
    sortby: list
    page_size: int
    language: str
    search: str # search keywords, should match relevance sortby
    user: str # Display kernels by a particular group
    kernel_type: str # Display kernels of a specific type
    output_type: str # Display kernels with a specific output type
    dataset: str # Display kernels using the specified dataset
    competition: str # Display kernels using the specified competition
    page: int # Page number


    def __init__(self, notebooks_dir = "notebooks"):
        self.page_size = 100
        self.language = "python"
        self.notebooks_dir = notebooks_dir
        self.kernel_types = ['all', 'script', 'notebook']
        self.output_types = ['all', 'visualization', 'data']

    def download_list_of_kernels(self,pid: int, sortby: str) -> list:
        print(f"Download list kernels with page pid {pid}")
        return kaggle.api.kernels_list(language=self.language, page_size=self.page_size, page=pid, sort_by=sortby)

    def download_list_of_kernels_by_dataset(self,pid: int, dataset_ref: str) -> list:
        print(f"Download list kernels with page pid {pid}")
        return kaggle.api.kernels_list(language=self.language, page_size=self.page_size, page=pid, dataset=dataset_ref)

    def download_list_of_kernels_by_user(self,pid: int, user_ref: str) -> list:
        print(f"Download list kernels with page pid {pid}")
        return kaggle.api.kernels_list(language=self.language, page_size=self.page_size, page=pid, user=user_ref)

    def download_list_of_datasets(self, pid: int, sortby: str) -> list:
        print(f"Download list datasets with page pid {pid}")
        return kaggle.api.dataset_list(page=pid,sort_by=sortby)

    def download_kernel(self, kernel_ref:str):
        try:
            print(f"download kernel {kernel_ref}")
            kaggle.api.kernels_pull(kernel_ref, self.notebooks_dir + "/" + kernel_ref, metadata=True)
        except:
            print(f"problem with downloading kernel {kernel_ref}")


if __name__ == "__main__":
    downloader = kaggle_downloader()
    #print(downloader.print_sortby())
    #st = downloader.download_list_of_kernels(1,8)
    #print(st)
    #print(type(st))
    kr = "pmarcelino/comprehensive-data-exploration-with-python"
    downloader.download_kernel(kr)
