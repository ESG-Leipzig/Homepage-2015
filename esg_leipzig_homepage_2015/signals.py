def mediafile_delete(sender, instance, **kwargs):
    # Pass False so FileField doesn't save the model.
    instance.mediafile.delete(save=False)
