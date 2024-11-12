from importlib.metadata import version
import transformers

from pyramidkv.llama_model import CustomLlamaAttention, LlamaSdpaAttention

from pyramidkv.mistral_model import mistral_flash_attn2_forward_PyramidKV,mistral_flash_attn2_forward_CAM,mistral_flash_attn2_forward_H2O,mistral_flash_attn2_forward_SnapKV,mistral_flash_attn2_forward_StreamingLLM
from pyramidkv.mistral_model import mistral_attn_forward_PyramidKV,mistral_attn_forward_CAM,mistral_attn_forward_H2O,mistral_attn_forward_SnapKV,mistral_attn_forward_StreamingLLM
from pyramidkv.mistral_model import mistral_sdpa_attn_forward_PyramidKV,mistral_sdpa_attn_forward_CAM,mistral_sdpa_attn_forward_H2O,mistral_sdpa_attn_forward_SnapKV,mistral_sdpa_attn_forward_StreamingLLM

from pyramidkv.llama_model import prepare_inputs_for_generation_llama, prepare_inputs_for_generation_llama_new
from pyramidkv.mistral_model import prepare_inputs_for_generation_mistral, prepare_inputs_for_generation_mistral_new


def replace_llama(config):
   
    print("Using PyramidKV!")
    transformers.models.llama.modeling_llama.LlamaForCausalLM.prepare_inputs_for_generation = prepare_inputs_for_generation_llama_new
    transformers.models.llama.modeling_llama.LlamaAttention.forward = CustomLlamaAttention.forward
    transformers.models.llama.modeling_llama.LlamaSdpaAttention.forward = LlamaSdpaAttention.forward

    # elif method == "streamingllm":
    #     print("Using StreamingLLM!")
    #     transformers.models.llama.modeling_llama.LlamaAttention.forward = llama_attn_forward_StreamingLLM
    #     transformers.models.llama.modeling_llama.LlamaFlashAttention2.forward = llama_flash_attn2_forward_StreamingLLM
    #     transformers.models.llama.modeling_llama.LlamaSdpaAttention.forward = llama_sdpa_attn_forward_StreamingLLM
        
    # elif method == "h2o":
    #     print("Using H2O!")
    #     transformers.models.llama.modeling_llama.LlamaAttention.forward = llama_attn_forward_H2O
    #     transformers.models.llama.modeling_llama.LlamaFlashAttention2.forward = llama_flash_attn2_forward_H2O
    #     transformers.models.llama.modeling_llama.LlamaSdpaAttention.forward = llama_sdpa_attn_forward_H2O
    
    # elif method == "cam":
    #     print("Using CAM!")
    #     transformers.models.llama.modeling_llama.LlamaAttention.forward = llama_attn_forward_CAM
    #     transformers.models.llama.modeling_llama.LlamaFlashAttention2.forward = llama_flash_attn2_forward_CAM
    #     transformers.models.llama.modeling_llama.LlamaSdpaAttention.forward = llama_sdpa_attn_forward_CAM
        
    # elif method == "snapkv":
    #     print("Using SnapKV!")
    #     transformers.models.llama.modeling_llama.LlamaAttention.forward = llama_attn_forward_SnapKV
    #     transformers.models.llama.modeling_llama.LlamaFlashAttention2.forward = llama_flash_attn2_forward_SnapKV
    #     transformers.models.llama.modeling_llama.LlamaSdpaAttention.forward = llama_sdpa_attn_forward_SnapKV
        
        
    # if method not in ["fullkv"]:


    


def replace_mistral(method):
    
    if method == "pyramidkv":
        print("Using PyramidKV!")
        transformers.models.mistral.modeling_mistral.MistralAttention.forward = mistral_attn_forward_PyramidKV
        transformers.models.mistral.modeling_mistral.MistralFlashAttention2.forward = mistral_flash_attn2_forward_PyramidKV
        transformers.models.mistral.modeling_mistral.MistralSdpaAttention.forward = mistral_sdpa_attn_forward_PyramidKV
    
    elif method == "streamingllm":
        print("Using StreamingLLM!")
        transformers.models.mistral.modeling_mistral.MistralAttention.forward = mistral_attn_forward_StreamingLLM
        transformers.models.mistral.modeling_mistral.MistralFlashAttention2.forward = mistral_flash_attn2_forward_StreamingLLM
        transformers.models.mistral.modeling_mistral.MistralSdpaAttention.forward = mistral_sdpa_attn_forward_StreamingLLM
        
    elif method == "h2o":
        print("Using H2O!")
        transformers.models.mistral.modeling_mistral.MistralAttention.forward = mistral_attn_forward_H2O
        transformers.models.mistral.modeling_mistral.MistralFlashAttention2.forward = mistral_flash_attn2_forward_H2O
        transformers.models.mistral.modeling_mistral.MistralSdpaAttention.forward = mistral_sdpa_attn_forward_H2O

    elif method == "cam":
        print("Using CAM!")
        transformers.models.llama.modeling_llama.LlamaAttention.forward = llama_attn_forward_CAM
        transformers.models.llama.modeling_llama.LlamaFlashAttention2.forward = llama_flash_attn2_forward_CAM
        transformers.models.llama.modeling_llama.LlamaSdpaAttention.forward = llama_sdpa_attn_forward_CAM
        
    elif method == "snapkv":
        print("Using SnapKV!")
        transformers.models.mistral.modeling_mistral.MistralAttention.forward = mistral_attn_forward_SnapKV
        transformers.models.mistral.modeling_mistral.MistralFlashAttention2.forward = mistral_flash_attn2_forward_SnapKV
        transformers.models.mistral.modeling_mistral.MistralSdpaAttention.forward = mistral_sdpa_attn_forward_SnapKV
        
        
    if method not in ["fullkv"]:
        transformers.models.mistral.modeling_mistral.MistralForCausalLM.prepare_inputs_for_generation = prepare_inputs_for_generation_mistral_new
