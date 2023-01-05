
FROM  continuumio/miniconda3
LABEL Author=LianosK

#---------------- Setup directories inside the container + copy project
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . $APP_HOME

#---------------- Prepare the envirennment
RUN chmod +x boot.sh
RUN conda env create --file environment.yml
SHELL ["/bin/bash", "-c", "source activate thesis-env"]
ENV PATH /opt/conda/envs/thesis-env/bin:$PATH

#---------------- Expose the necessary port
EXPOSE 5000

#---------------- Run script, that starts prod server
ENTRYPOINT ["./boot.sh"]

