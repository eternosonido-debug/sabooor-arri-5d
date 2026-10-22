# Sabooor ARRI — comunidade Canon / Magic Lantern

[Português (Brasil)](#sabooor-arri--comunidade-canon--magic-lantern) · [English](#english) · [T3i / 600D](https://github.com/eternosonido-debug/sabooor-arri-600d)

Port do visual Sabooor ARRI para modelos Canon com Magic Lantern, começando pela **EOS 5D Mark III**. O nome do repositório foi preservado; a arquitetura usa perfis explícitos para receber outros modelos depois de revisão.

**Estado: versão experimental de desenvolvimento. 5D3 1.1.3 e 1.2.3 compiladas no computador; teste físico pendente. Outros modelos ainda não recebem suporte por apenas existirem na árvore upstream.**

## Implementado na 5D Mark III

- Menu inspirado no mapa ALEXA 35, HOME, navegação e acesso ao menu original por INFO.
- Monitor com moldura preta, REC/STBY, exposição, espaço do cartão ativo e identificação full frame.
- Guias 16:9, 2,35:1, 1:1 e 9:16; controles nativos disponíveis ligados pelo nome original do ML.
- Look com emulações Fuji Provia, Velvia e Superia para prévia LCD, intensidade e integração anamórfica, condicionado ao formato de buffer suportado.
- Fontes de monitor derivadas de FiraGO sob SIL OFL: nenhuma fonte DIN proprietária é distribuída.

## Diferença importante da 600D

Na 5D3, Recording Resolution e Project Rate abrem o menu Canon, onde se escolhem resolução, cadência e ALL-I/IPB. O mod **não** reutiliza os setters e tamanhos de propriedades da 600D. O upstream alerta para cabeçalhos de vídeo corrompidos ao alternar certos modos em LiveView na DIGIC V. Zoom LCD usa o controle nativo com bloqueio durante REC.

O Look não altera H.264 e não aplica LUT ao HDMI. Sua velocidade e estabilidade reais na 5D3 ainda precisam de teste. RAW/MLV continua a cargo dos módulos originais; esta entrega não valida todas as combinações de módulos.

## Código completo e compilação

O patch versionado contém o código e recursos do mod. O preparador baixa a base GPL exata descrita em `upstream.json` e aplica o patch com verificação de integridade, reconstruindo a árvore completa.

```sh
python3 prepare.py source
export ARM_BINPATH=/caminho/arm-gnu-toolchain/bin
sh source/tools/build-sabooor-community.sh 5D3.113 -j4
# ou, separadamente, para firmware Canon 1.2.3:
sh source/tools/build-sabooor-community.sh 5D3.123 -j4
```

Dependências: Git, Make, compilador C do computador, Python 3 e toolchain ARM bare-metal. A validação local usou Arm GNU 13.2.Rel1. Pillow é necessário para os testes de renderização e para gerar as fontes; instalar com `python3 -m pip install Pillow` em ambiente virtual. Leia `docs/VALIDACAO.md` e `docs/INSTALACAO.md` antes de preparar um cartão.

## Testes no computador

```sh
cd source
SABOOOR_TEST_PLATFORM=5D3.113 python3 tests/sabooor/test_camera_controls.py
SABOOOR_TEST_PLATFORM=5D3.113 python3 tests/sabooor/test_runtime.py
SABOOOR_TEST_PLATFORM=5D3.113 python3 tests/sabooor/test_exact_map.py ../render-5d3
```

Repita para 5D3.123. Os mesmos testes aceitam 600D.102 para regressão. São testes do código C com entradas de câmera simuladas; não emulam o hardware Canon.

Consulte `docs/MODELOS.json`, `docs/ROADMAP.md` e `docs/PORTABILIDADE.md`. Código sob GPL-2.0-or-later, fontes FiraGO sob SIL OFL e gerador de emulações sob MIT, com avisos incluídos no patch. Projeto independente, sem afiliação à Canon, ARRI ou Fujifilm.

## Pacotes experimentais

[5D3 firmware 1.1.3](dist/sabooor-arri-5D3.113-experimental.zip) · [5D3 firmware 1.2.3](dist/sabooor-arri-5D3.123-experimental.zip) · [SHA256](dist/SHA256SUMS.txt). Usar somente com Magic Lantern já funcional no firmware exato, após ler as instruções. Não são builds estáveis validados em câmera.

![HOME renderizada pelo código com dados simulados; não é foto da câmera](docs/images/home-5d3-123.png)

## English

Sabooor ARRI is a community visual mod for Canon cameras running Magic Lantern, starting with the **EOS 5D Mark III, Canon firmware 1.1.3 and 1.2.3**. Separate builds exist for each firmware. Other Canon models remain planned and unreviewed; their presence in the upstream source does not mean Sabooor support.

The mod brings an ALEXA 35 menu-map-inspired interface, HOME screen, black monitoring frame with REC/STBY, exposure and active-card information, full-frame identification and 16:9 / 2.35:1 / 1:1 / 9:16 guides. Available controls use original ML callbacks; unavailable functions remain N/A. INFO opens the original ML presentation.

**Experimental developer builds: ARM compilation and host code tests passed; physical camera validation is pending.** The assistant has not tested boot, recording, audio, HDMI, temperature or LUT performance on a physical 5D3. RAW/MLV modules remain upstream features; all module combinations have not been validated.

On the 5D3, **Recording Resolution and Project Rate open Canon's own menu** for resolution, cadence and ALL-I/IPB. This port does not reuse the 600D video-property setters: upstream warns about corrupted movie headers when switching certain modes in LiveView on DIGIC V. Native LCD zoom is guarded during recording.

Look includes creative Fuji Provia, Velvia and Superia film emulations with intensity and anamorphic preview integration. **LCD preview only: no grading of recorded H.264 and no HDMI LUT processing.** These are not official Fujifilm simulations. Unsupported display-buffer dimensions disable Look. Monitor and menu fonts are redistributable FiraGO under SIL OFL; proprietary DIN files are excluded.

### Downloads and installation

[5D3 Canon 1.1.3](dist/sabooor-arri-5D3.113-experimental.zip) · [5D3 Canon 1.2.3](dist/sabooor-arri-5D3.123-experimental.zip) · [SHA256](dist/SHA256SUMS.txt).

For contributors with working Magic Lantern on the **exact matching firmware**. Packages have no FIR installer and do not modify bootflags. Back up the current autoexec.bin, matching ML/modules/5D3_113.sym or 5D3_123.sym, fonts and settings. Verify the checksum, copy the package while preserving paths, keep DCIM and other files, safely eject and insert with the camera off. Select Prefs > Sabooor ARRI > Monitor or HOME; default remains Original. Test menus, then a short clip and inspect it on a computer. To revert, restore the previous core, symbols and fonts together. Do not mix targets, format the card or attempt a Canon firmware upgrade/downgrade using these packages.

### Source, build and validation

prepare.py verifies the patch checksum and reconstructs the full GPL source using the pinned upstream revision in upstream.json.

```sh
python3 prepare.py source
export ARM_BINPATH=/path/to/arm-gnu-toolchain/bin
sh source/tools/build-sabooor-community.sh 5D3.113 -j4
# Use 5D3.123 separately for Canon firmware 1.2.3.
```

Requires Git, Make, Python 3 and an ARM bare-metal toolchain; local validation used Arm GNU 13.2.Rel1. Host rendering tests require Pillow and a C compiler. Run the tests above with SABOOOR_TEST_PLATFORM=5D3.113 or 5D3.123; 600D.102 is the regression reference. These tests execute C code with mocked camera I/O, not Canon hardware emulation. The source patch was applied to a clean pinned base and all 50 changed files matched byte-for-byte.

Source is GPL-2.0-or-later; FiraGO is SIL OFL and the film emulation generator is MIT. Notices are included. This independent project is not affiliated with Canon, ARRI or Fujifilm. See docs/MODELOS.json for the model matrix and docs/VALIDACAO.md for detailed validation records.
