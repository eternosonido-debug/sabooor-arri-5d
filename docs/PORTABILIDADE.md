# Arquitetura do port

`src/sabooor-platform.h` habilita explicitamente 600D e os firmwares 5D3 1.1.3/1.2.3. Modelo, firmware, sensor e estratégia de controle de vídeo são definidos por perfil. A renderização de menu e monitor é compartilhada; os callbacks originais do ML mantêm propriedade, configuração e hierarquia.

5D3: sensor full frame, LCD 3:2 segundo os internals upstream; botões RATE/M-Fn substituem os rótulos DISP/Av da 600D na apresentação. Isso não remapeia botões físicos. O cartão ativo é obtido pela API do ML, sem presumir SD ou CF.

Resolução/cadência: a 600D mantém seus seletores existentes; a 5D3 delega ao menu Canon para evitar transportar setters ainda não validados. A prévia LUT aceita somente buffers UYVY 720x480/pitch1440 e desliga o Look se não reconhecer o modo. HDMI não recebe processamento LUT.

Fontes: o gerador público deriva os RBFs dos mesmos bitmaps FiraGO OFL já usados pelo menu. Não depende de arquivos DIN locais. Outros modelos ficam com o comportamento original do ML e tema inativo.

Boot: nenhuma instrução/endereço de inicialização ou reserva do upstream 5D3 foi modificada. DIGIC V usa a reserva dinâmica do caminho boot-d45; o limite específico 0xD00000 da 600D não é aplicado à 5D3. O tamanho estático é relatado, sem alegar validação de heap físico.
