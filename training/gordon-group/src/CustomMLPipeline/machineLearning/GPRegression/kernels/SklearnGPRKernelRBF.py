def build(this):
    """
    This effectively constructs the type instance, by creating the object to be placed in the kernel field. Ideally this should be replaced by a callback function (beforeMake or afterMake).
    """
    from sklearn.gaussian_process.kernels import RBF

    sklKernel = RBF(length_scale=this.lengthScale)

    kernel_pickled = c3.PythonSerialization.serialize(obj=sklKernel)
    kernel_name = 'RBF'
    kernel_hyperParameters = [this.lengthScale]

    this.kernel = c3.SklearnGPRKernel(
        name=kernel_name,
        hyperParameters=kernel_hyperParameters,
        pickledKernel=kernel_pickled
    )

    return this