# Local development patch: avoid blocking DNS lookups in jekyll-github-metadata
# when the environment has restricted network access.
module Jekyll
  module GitHubMetadata
    class Client
      def internet_connected?
        false
      end
    end
  end
end
