using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.FeatureManagement;

namespace YourProjectName.Pages
{
    public class IndexModel : PageModel
    {
        private readonly IFeatureManager _featureManager;

        public IndexModel(IFeatureManager featureManager)
        {
            _featureManager = featureManager;
        }

        public string FeatureAMessage { get; set; }
        public string FeatureBMessage { get; set; }

        public async Task OnGet()
        {
            // Check if FeatureA is enabled
            if (await _featureManager.IsEnabledAsync("FeatureA"))
            {
                FeatureAMessage = "FeatureA is enabled!";
            }
            else
            {
                FeatureAMessage = "FeatureA is disabled!";
            }

            // Check if FeatureB is enabled
            if (await _featureManager.IsEnabledAsync("FeatureB"))
            {
                FeatureBMessage = "FeatureB is enabled!";
            }
            else
            {
                FeatureBMessage = "FeatureB is disabled!";
            }
        }
    }
}
