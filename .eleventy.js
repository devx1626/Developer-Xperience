// Eleventy configuration - see https://www.11ty.dev/docs/config/
module.exports = function (eleventyConfig) {
  // Absolute origin used for canonical URLs and Open Graph images.
  // Set SITE_URL (e.g. https://developer-xperience.example) when deploying.
  eleventyConfig.addGlobalData('siteUrl', () => process.env.SITE_URL || '');

  return {
    dir: {
      input: 'src',   // templates live here (content is DRY via _includes)
      output: '.',    // generated HTML goes to the project root, next to assets
    },
  };
};
