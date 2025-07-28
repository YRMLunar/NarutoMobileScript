// uno.config.ts
// uno.config.ts
import {
  defineConfig,
  presetAttributify,
  presetIcons,
  presetTypography,
  presetUno,
  presetWebFonts,
  transformerDirectives,
  transformerVariantGroup,
} from 'unocss';

// 定义主色调或从其他地方导入
const primaryColor = '#1890ff';

export default defineConfig({
  theme: {
    colors: {
      primary: primaryColor,
      white: '#ffffff',
      neutral: '#C4C4C4',
      dark: '#2f3136',
      slate: '#020617',
    },
  },
  presets: [presetUno(), presetAttributify(), presetIcons(), presetTypography(), presetWebFonts()],
  transformers: [transformerDirectives(), transformerVariantGroup()],
});
