class load_model:

   model_id='Codellama/codeLlama-7b-hf'
  #model_id='pytorch_model-00007-of-00007.bin'
   hf_auth='xxxxx'
   device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'


    def __init__(self):
        """
        __init__ method of load model Class


        """

        
        bnb_config = transformers.BitsAndBytesConfig(
                      load_in_4bit=True,
                      bnb_4bit_quant_type='nf4',
                      bnb_4bit_use_double_quant=True,
                      bnb_4bit_compute_dtype=bfloat16
                       )
        self._max_retries=5
        self.model_config = transformers.AutoConfig.from_pretrained(
                                self.model_id,
                                use_auth_token=self.hf_auth)
        
        self.model = AutoModelForCausalLM.from_pretrained(self.model_id,
                      trust_remote_code=True,
                      config=self.model_config,
                      quantization_config=bnb_config,
                      device_map=self.device
                      use_auth_token=self.hf_auth

                  )
    def pipelining(self,query):
      pipeline=pipeline('text-generation',
                      model=self.model
                      )
      code=pipeline('def merge2csv(',temperature=0.2)
      print(code)






