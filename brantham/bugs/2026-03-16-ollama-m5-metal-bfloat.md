# Bug: Ollama 0.18.0 crash Metal sur M5/macOS Tahoe

## Symptome
Toute inference via Ollama retourne 500 avec erreur Metal shader:
```
MTLLibraryErrorDomain Code=3
static_assert failed: __tensor_ops_detail::__is_same_v<bfloat, half>
"Input types must match cooperative tensor types"
ggml_metal_init: error: failed to initialize the Metal library
```

## Cause
macOS 26 (Tahoe) + Apple M5 : MetalPerformancePrimitives.framework a un bug de type matching bfloat/half dans les matmul2d cooperative tensor ops. Affecte TOUS les modeles (qwen2.5:7b, 0.5b).

## Workaround
Utiliser `llama-cpp-python` au lieu d'Ollama. llama-cpp-python skip gracieusement les kernels bf16 non supportes:
```
ggml_metal_init: skipping kernel_mul_mv_bf16_f32 (not supported)
```

## Impact
- Ollama inutilisable tant que le bug Metal M5 n'est pas fix upstream
- llama-cpp-python fonctionne avec Metal (fp16/fp32) mais pas bf16
- Performance: ~8 tok/s avec Metal partiel (vs ~40 tok/s attendu avec full Metal)

## Tags
ollama, metal, m5, macos-tahoe, llama-cpp-python

## Related
- [[brantham/_MOC]]
- [[website/sessions/2026-03-16]]
- [[website/sessions/2026-03-16-accent-fix]]
- [[website/sessions/2026-03-16-seo-audit-t01]]
- [[brantham/bugs/2026-03-16-probability-matrix-oscillation]]
- [[brantham/sessions/2026-03-16]]
