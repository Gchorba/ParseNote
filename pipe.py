



<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>onenotepipe/pipe.py at master · hirenj/onenotepipe</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="hirenj/onenotepipe" name="twitter:title" /><meta content="onenotepipe - Tool to get files from html into OneNote" name="twitter:description" /><meta content="https://avatars2.githubusercontent.com/u/155605?v=3&amp;s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars2.githubusercontent.com/u/155605?v=3&amp;s=400" property="og:image" /><meta content="hirenj/onenotepipe" property="og:title" /><meta content="https://github.com/hirenj/onenotepipe" property="og:url" /><meta content="onenotepipe - Tool to get files from html into OneNote" property="og:description" />

      <meta name="browser-stats-url" content="/_stats">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    <link rel="xhr-socket" href="/_sockets">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="81A14468:706F:1AE8CC2A:5468D49F" name="octolytics-dimension-request_id" /><meta content="7267146" name="octolytics-actor-id" /><meta content="Gchorba" name="octolytics-actor-login" /><meta content="7c2aeb4302168608c79a3d911fc3894ad72757736e98d6149620c3b1d3c3bb1f" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="Uen1ZogumiD8qOgEerQCKajn8fZFdYcGYZjrSnptuj6bnbNSE4h2OTNOTUuYCj2vrR/2jsbFpEAtOzQE5cHCvg==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-59da74dcbe2f1d555e306461652274f8741238a64e7b1fe8cc5a286232044835.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-22a0054564248c6dd87336e91bca068b1ab49e28ee1062519b3a0722d29da804.css" media="all" rel="stylesheet" type="text/css" />
    
    


    <meta http-equiv="x-pjax-version" content="f3f7311a29adcb300a5a91e93e68baf2">

      
  <meta name="description" content="onenotepipe - Tool to get files from html into OneNote">
  <meta name="go-import" content="github.com/hirenj/onenotepipe git https://github.com/hirenj/onenotepipe.git">

  <meta content="155605" name="octolytics-dimension-user_id" /><meta content="hirenj" name="octolytics-dimension-user_login" /><meta content="24191493" name="octolytics-dimension-repository_id" /><meta content="hirenj/onenotepipe" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="24191493" name="octolytics-dimension-repository_network_root_id" /><meta content="hirenj/onenotepipe" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/hirenj/onenotepipe/commits/master.atom" rel="alternate" title="Recent Commits to onenotepipe:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" ga-data-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/hirenj/onenotepipe/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/hirenj/onenotepipe/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
      </div>
      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item explore">
          <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>
        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>
          </li>
        <li class="header-nav-item">
          <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
        </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name" href="/Gchorba" data-ga-click="Header, go to profile, text:username">
      <img alt="Gene Chorba" class="avatar" data-user="7267146" height="20" src="https://avatars3.githubusercontent.com/u/7267146?v=3&amp;s=40" width="20" />
      <span class="css-truncate">
        <span class="css-truncate-target">Gchorba</span>
      </span>
    </a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link js-menu-target tooltipped tooltipped-s" href="#" aria-label="Create new..." data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      
<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="dropdown-divider"></li>
    <li class="dropdown-header">
      <span title="hirenj/onenotepipe">This repository</span>
    </li>
      <li>
        <a href="/hirenj/onenotepipe/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
</ul>

    </div>
  </li>

  <li class="header-nav-item">
        <a href="/notifications" aria-label="You have no unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:read" data-hotkey="g n">
        <span class="mail-status all-read"></span>
        <span class="octicon octicon-inbox"></span>
</a>
  </li>

  <li class="header-nav-item">
    <a class="header-nav-link tooltipped tooltipped-s" href="/settings/profile" id="account_settings" aria-label="Settings" data-ga-click="Header, go to settings, icon:settings">
      <span class="octicon octicon-gear"></span>
    </a>
  </li>

  <li class="header-nav-item">
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="C3d0H+giTIVnG+UaNFTmlSEJns9Cn0aUrCTuFNkXT+gwZKbtw2YzXXO+/1t/XcfoF71i1DL0i4iyQvstd1NbzA==" /></div>
      <button class="header-nav-link sign-out-button tooltipped tooltipped-s" aria-label="Sign out" data-ga-click="Header, sign out, icon:logout">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>


    
  </div>
</div>

      

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="UxGxNAN4SUkuzK+hPsRpQ/Ifdw609HVYGX2b/zhHvGgY0/xy9gV0PX7tFG9cipkHBkloeFXqz+H+Xt4Asc4jpw==" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="24191493" />

    <div class="select-menu js-menu-container js-select-menu">
      <a class="social-count js-social-count" href="/hirenj/onenotepipe/watchers">
        1
      </a>
      <a href="/hirenj/onenotepipe/subscription"
        class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true">
        <span class="js-select-button">
          <span class="octicon octicon-eye"></span>
          Watch
        </span>
      </a>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
            <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">Be notified when participating or @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">Be notified of all conversations.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">Never be notified.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/hirenj/onenotepipe/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="R63lhFEjmr7HDQARUiKiqn0bIoMNszWf79E/1WBGG+DP7JgOVhwH9F3iGUVmRpsthh4LJAOyQISsMS7lAp+baA==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Unstar this repository" title="Unstar hirenj/onenotepipe">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/hirenj/onenotepipe/stargazers">
          0
        </a>
</form>
    <form accept-charset="UTF-8" action="/hirenj/onenotepipe/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="98rVfRba2TbQdJOgGTC/TBybuMSJcO/3rbWoP5tBLxRZ2HgfMaPstrxCZxN0WAU9Yja4S6fH+VeWYQABxbUpCw==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Star this repository" title="Star hirenj/onenotepipe">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/hirenj/onenotepipe/stargazers">
          0
        </a>
</form>  </div>

  </li>


        <li>
          <a href="/hirenj/onenotepipe/fork" class="minibutton with-count js-toggler-target fork-button tooltipped-n" title="Fork your own copy of hirenj/onenotepipe to your account" aria-label="Fork your own copy of hirenj/onenotepipe to your account" rel="nofollow" data-method="post">
            <span class="octicon octicon-repo-forked"></span>
            Fork
          </a>
          <a href="/hirenj/onenotepipe/network" class="social-count">0</a>
        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/hirenj" class="url fn" itemprop="url" rel="author"><span itemprop="title">hirenj</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/hirenj/onenotepipe" class="js-current-repository" data-pjax="#js-repo-pjax-container">onenotepipe</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/hirenj/onenotepipe/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/hirenj/onenotepipe" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /hirenj/onenotepipe">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/hirenj/onenotepipe/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /hirenj/onenotepipe/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
      <a href="/hirenj/onenotepipe/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /hirenj/onenotepipe/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>


      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/hirenj/onenotepipe/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /hirenj/onenotepipe/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/hirenj/onenotepipe/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /hirenj/onenotepipe/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/hirenj/onenotepipe/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /hirenj/onenotepipe/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>
  </ul>


</nav>

              <div class="only-with-full-nav">
                
  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="https://github.com/hirenj/onenotepipe.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/hirenj/onenotepipe.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="git@github.com:hirenj/onenotepipe.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="git@github.com:hirenj/onenotepipe.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="https://github.com/hirenj/onenotepipe" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/hirenj/onenotepipe" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>


  <a href="http://windows.github.com" class="minibutton sidebar-button" title="Save hirenj/onenotepipe to your computer and use it in GitHub Desktop." aria-label="Save hirenj/onenotepipe to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/hirenj/onenotepipe/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download the contents of hirenj/onenotepipe as a zip file"
                   title="Download the contents of hirenj/onenotepipe as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/hirenj/onenotepipe/blob/24eafac917e023fddef19ba0b44513738b95188b/pipe.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:37f78bb7708d63db8ce4dfdf8eee86e5 -->

<div class="file-navigation">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/hirenj/onenotepipe/blob/master/pipe.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="button-group right">
    <a href="/hirenj/onenotepipe/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="pipe.py" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/hirenj/onenotepipe" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">onenotepipe</span></a></span></span><span class="separator"> / </span><strong class="final-path">pipe.py</strong>
  </div>
</div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="Hiren Joshi" class="avatar" data-user="155605" height="24" src="https://avatars0.githubusercontent.com/u/155605?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/hirenj" rel="author">hirenj</a></span>
        <time datetime="2014-09-18T14:33:17Z" is="relative-time">Sep 18, 2014</time>
        <div class="commit-title">
            <a href="/hirenj/onenotepipe/commit/24eafac917e023fddef19ba0b44513738b95188b" class="message" data-pjax="true" title="Basic implementation of the pipe">Basic implementation of the pipe</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>1</strong>
           contributor
        </a>
      </p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="Hiren Joshi" data-user="155605" height="24" src="https://avatars0.githubusercontent.com/u/155605?v=3&amp;s=48" width="24" />
            <a href="/hirenj">hirenj</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
          <span class="mode" title="File mode">executable file</span>
          <span class="meta-divider"></span>
          <span>253 lines (207 sloc)</span>
          <span class="meta-divider"></span>
        <span>8.91 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
          <a href="/hirenj/onenotepipe/raw/master/pipe.py" class="minibutton " id="raw-url">Raw</a>
            <a href="/hirenj/onenotepipe/blame/master/pipe.py" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/hirenj/onenotepipe/commits/master/pipe.py" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->

          <a class="octicon-button tooltipped tooltipped-nw"
             href="http://windows.github.com" aria-label="Open this file in GitHub for Windows">
              <span class="octicon octicon-device-desktop"></span>
          </a>

              <a class="octicon-button tooltipped tooltipped-n js-update-url-with-hash"
                 aria-label="Clicking this button will fork this project so you can edit the file"
                 href="/hirenj/onenotepipe/edit/master/pipe.py"
                 data-method="post" rel="nofollow"><span class="octicon octicon-pencil"></span></a>

            <a class="octicon-button danger tooltipped tooltipped-s"
               href="/hirenj/onenotepipe/delete/master/pipe.py"
               aria-label="Fork this project and delete file"
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">
          <span class="octicon octicon-trashcan"></span>
        </a>
      </div><!-- /.actions -->
    </div>
    

  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size-8 js-file-line-container">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code js-file-line"><span class="pl-c"><span class="pl-pdc">#</span>!/usr/bin/env python</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code js-file-line"><span class="pl-k">import</span> keyring</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code js-file-line"><span class="pl-k">import</span> getpass</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code js-file-line"><span class="pl-k">import</span> ConfigParser</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code js-file-line"><span class="pl-k">import</span> tempfile,os,sys</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code js-file-line"><span class="pl-k">import</span> xattr</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code js-file-line"><span class="pl-k">import</span> iso8601</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code js-file-line"><span class="pl-k">import</span> calendar</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code js-file-line"><span class="pl-k">from</span> datetime <span class="pl-k">import</span> datetime</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code js-file-line"><span class="pl-k">from</span> onedrive.api_v5 <span class="pl-k">import</span> OneDriveAuth</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code js-file-line"><span class="pl-k">import</span> signal</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code js-file-line"><span class="pl-k">import</span> BaseHTTPServer</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code js-file-line"><span class="pl-k">import</span> functools <span class="pl-k">as</span> ft</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code js-file-line"><span class="pl-k">import</span> urllib</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code js-file-line"><span class="pl-k">import</span> urlparse</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code js-file-line"><span class="pl-k">import</span> json</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code js-file-line"><span class="pl-k">import</span> types</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code js-file-line"><span class="pl-k">import</span> lxml</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code js-file-line"><span class="pl-k">import</span> lxml.html</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code js-file-line"><span class="pl-k">from</span> lxml <span class="pl-k">import</span> etree</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code js-file-line"><span class="pl-k">import</span> mimetypes</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code js-file-line"><span class="pl-k">import</span> collections</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code js-file-line"><span class="pl-k">from</span> StringIO <span class="pl-k">import</span> StringIO</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code js-file-line"><span class="pl-k">import</span> string</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code js-file-line"><span class="pl-k">import</span> random</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code js-file-line"><span class="pl-k">import</span> sys</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code js-file-line"><span class="pl-k">from</span> optparse <span class="pl-k">import</span> OptionParser</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code js-file-line"><span class="pl-s">global</span> interrupted</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code js-file-line">interrupted <span class="pl-ko">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code js-file-line">auth_code <span class="pl-ko">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code js-file-line"><span class="pl-s">class</span> <span class="pl-entc">AuthenticationError</span>(<span class="pl-eoi"><span class="pl-st">Exception</span></span>):</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code js-file-line">    <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code js-file-line"><span class="pl-s">class</span> <span class="pl-entc">AuthHandler</span>(<span class="pl-eoi">BaseHTTPServer.BaseHTTPRequestHandler</span>):</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code js-file-line">    <span class="pl-s">def</span> <span class="pl-enf">do_HEAD</span>(<span class="pl-vpf">s</span>):</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code js-file-line">        s.send_response(<span class="pl-cn">200</span>)</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code js-file-line">        s.send_header(<span class="pl-s1"><span class="pl-pds">&quot;</span>Content-type<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>text/html<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code js-file-line">        s.end_headers()</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code js-file-line">    <span class="pl-s">def</span> <span class="pl-enf">do_GET</span>(<span class="pl-vpf">s</span>):</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code js-file-line">        <span class="pl-s">global</span> auth_code</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code js-file-line">        <span class="pl-s">global</span> KEEP_RUNNING</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code js-file-line">        KEEP_RUNNING <span class="pl-ko">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code js-file-line">        <span class="pl-s1"><span class="pl-pds">&quot;&quot;&quot;</span>Respond to a GET request.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code js-file-line">        s.send_response(<span class="pl-cn">200</span>)</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code js-file-line">        s.send_header(<span class="pl-s1"><span class="pl-pds">&quot;</span>Content-type<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>text/html<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code js-file-line">        s.end_headers()</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code js-file-line">        s.wfile.write(<span class="pl-s1"><span class="pl-pds">&quot;</span>&lt;html&gt;&lt;head&gt;&lt;title&gt;Authorization successful&lt;/title&gt;&lt;/head&gt;<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code js-file-line">        s.wfile.write(<span class="pl-s1"><span class="pl-pds">&quot;</span>&lt;body&gt;&lt;p&gt;Successfully authorized&lt;/p&gt;<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code js-file-line">        auth_code <span class="pl-ko">=</span> s.path</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code js-file-line">        s.wfile.write(<span class="pl-s1"><span class="pl-pds">&quot;</span>&lt;/body&gt;&lt;/html&gt;<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code js-file-line"><span class="pl-s">def</span> <span class="pl-enf">signal_handler</span>(<span class="pl-vpf">signal</span>, <span class="pl-vpf">frame</span>):</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code js-file-line">        <span class="pl-k">print</span> <span class="pl-ko">&gt;&gt;</span> sys.stderr, <span class="pl-s1"><span class="pl-pds">&#39;</span>Onenote pipe: Aborting<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code js-file-line">        interrupted <span class="pl-ko">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code js-file-line">        sys.exit(<span class="pl-cn">0</span>)</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code js-file-line">signal.signal(signal.SIGINT, signal_handler)</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code js-file-line"><span class="pl-s">def</span> <span class="pl-enf">main</span>():</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code js-file-line">    parser <span class="pl-ko">=</span> OptionParser()</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code js-file-line">    parser.add_option(<span class="pl-s1"><span class="pl-pds">&quot;</span>-c<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>--command<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">dest</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&quot;</span>command<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code js-file-line">                      <span class="pl-vpf">help</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&quot;</span>run COMMAND<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">metavar</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&quot;</span>COMMAND<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code js-file-line">    parser.add_option(<span class="pl-s1"><span class="pl-pds">&quot;</span>-n<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>--notebook<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">dest</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&quot;</span>notebook<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code js-file-line">                      <span class="pl-vpf">help</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&quot;</span>Specify notebook<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code js-file-line">    parser.add_option(<span class="pl-s1"><span class="pl-pds">&quot;</span>-s<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>--section<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">dest</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&quot;</span>section<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">help</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&quot;</span>Specify section<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code js-file-line">    parser.add_option(<span class="pl-s1"><span class="pl-pds">&quot;</span>-f<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>--filename<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">dest</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&quot;</span>filename<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">help</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&quot;</span>HTML file to read<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code js-file-line">    parser.add_option(<span class="pl-s1"><span class="pl-pds">&quot;</span>-q<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>--quiet<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code js-file-line">                      <span class="pl-vpf">action</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&quot;</span>store_false<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">dest</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&quot;</span>verbose<span class="pl-pds">&quot;</span></span>, <span class="pl-vpf">default</span><span class="pl-ko">=</span><span class="pl-c1">True</span>,</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code js-file-line">                      <span class="pl-vpf">help</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&quot;</span>don&#39;t print status messages to stdout<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code js-file-line">    (options, args) <span class="pl-ko">=</span> parser.parse_args()</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code js-file-line">    <span class="pl-s">global</span> verbose</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code js-file-line">    verbose <span class="pl-ko">=</span> options.verbose</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code js-file-line">    client <span class="pl-ko">=</span> get_client()</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code js-file-line">    <span class="pl-k">if</span> options.command <span class="pl-ko">==</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>login<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code js-file-line">        <span class="pl-k">print</span> client.auth_access_token</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code js-file-line">    <span class="pl-k">if</span> options.command <span class="pl-ko">==</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>notebooks<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code js-file-line">        get_notebooks(client)</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code js-file-line">    <span class="pl-k">if</span> options.command <span class="pl-ko">==</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>sections<span class="pl-pds">&quot;</span></span> :</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code js-file-line">        get_sections(client,options.notebook)</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code js-file-line">    <span class="pl-k">if</span> options.command <span class="pl-ko">==</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>upload<span class="pl-pds">&quot;</span></span> :</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code js-file-line">        write_page(client,options.notebook,options.section,options.filename)</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code js-file-line"><span class="pl-s">def</span> <span class="pl-enf">get_notebooks</span>(<span class="pl-vpf">client</span>):</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code js-file-line">    datas <span class="pl-ko">=</span> client.do_request(<span class="pl-vpf">url</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span>notebooks<span class="pl-pds">&#39;</span></span>, <span class="pl-vpf">query</span><span class="pl-ko">=</span>{<span class="pl-s1"><span class="pl-pds">&#39;</span>select<span class="pl-pds">&#39;</span></span> : <span class="pl-s1"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>})[<span class="pl-s1"><span class="pl-pds">&#39;</span>value<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code js-file-line">    notebooknames <span class="pl-ko">=</span> [ notebook[<span class="pl-s1"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>] <span class="pl-k">for</span> notebook <span class="pl-kolp">in</span> datas]</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code js-file-line">    <span class="pl-k">print</span> <span class="pl-s1"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>.join(notebooknames)</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code js-file-line"><span class="pl-s">def</span> <span class="pl-enf">get_sections</span>(<span class="pl-vpf">client</span>,<span class="pl-vpf">notebook_name</span>):</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code js-file-line">    datas <span class="pl-ko">=</span> client.do_request(<span class="pl-vpf">url</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span>notebooks<span class="pl-pds">&#39;</span></span>, <span class="pl-vpf">query</span><span class="pl-ko">=</span>{<span class="pl-s1"><span class="pl-pds">&#39;</span>filter<span class="pl-pds">&#39;</span></span> : <span class="pl-s1"><span class="pl-pds">&quot;</span>name eq <span class="pl-cce">\&#39;</span><span class="pl-c1">%s</span><span class="pl-cce">\&#39;</span><span class="pl-pds">&quot;</span></span> <span class="pl-ko">%</span> notebook_name, <span class="pl-s1"><span class="pl-pds">&#39;</span>select<span class="pl-pds">&#39;</span></span> : <span class="pl-s1"><span class="pl-pds">&quot;</span>id<span class="pl-pds">&quot;</span></span> })[<span class="pl-s1"><span class="pl-pds">&#39;</span>value<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code js-file-line">    <span class="pl-k">if</span> datas:</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code js-file-line">        datas <span class="pl-ko">=</span> client.do_request(<span class="pl-vpf">url</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span>notebooks/<span class="pl-c1">%s</span>/sections<span class="pl-pds">&#39;</span></span> <span class="pl-ko">%</span> datas[<span class="pl-cn">0</span>][<span class="pl-s1"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span>], <span class="pl-vpf">query</span><span class="pl-ko">=</span>{<span class="pl-s1"><span class="pl-pds">&#39;</span>select<span class="pl-pds">&#39;</span></span> : <span class="pl-s1"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>} )[<span class="pl-s1"><span class="pl-pds">&#39;</span>value<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code js-file-line">        sectionnames <span class="pl-ko">=</span> [ section[<span class="pl-s1"><span class="pl-pds">&#39;</span>name<span class="pl-pds">&#39;</span></span>] <span class="pl-k">for</span> section <span class="pl-kolp">in</span> datas]</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code js-file-line">        <span class="pl-k">print</span>  <span class="pl-s1"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span>.join(sectionnames)</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code js-file-line"><span class="pl-s">def</span> <span class="pl-enf">id_generator</span>(<span class="pl-vpf">size</span><span class="pl-ko">=</span><span class="pl-cn">6</span>, <span class="pl-vpf">chars</span><span class="pl-ko">=</span>string.ascii_uppercase <span class="pl-ko">+</span> string.digits):</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code js-file-line">    <span class="pl-k">return</span> <span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>.join(random.choice(chars) <span class="pl-k">for</span> _ <span class="pl-kolp">in</span> <span class="pl-sf">range</span>(size))</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code js-file-line"><span class="pl-s">def</span> <span class="pl-enf">read_html</span>(<span class="pl-vpf">filename</span>):</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code js-file-line">    parser <span class="pl-ko">=</span> etree.HTMLParser()</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code js-file-line">    tree <span class="pl-ko">=</span> etree.parse(<span class="pl-sf">open</span>(filename),parser)</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code js-file-line">    elements_to_read <span class="pl-ko">=</span> tree.xpath(<span class="pl-s1"><span class="pl-pds">&#39;</span>//img[not(starts-with(@src, &quot;http&quot;))]<span class="pl-pds">&#39;</span></span>) <span class="pl-ko">+</span> tree.xpath(<span class="pl-s1"><span class="pl-pds">&#39;</span>//object[starts-with(@data, &quot;file://&quot;)]<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code js-file-line">    to_attach <span class="pl-ko">=</span> []</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code js-file-line">    <span class="pl-k">if</span> <span class="pl-kolp">not</span> elements_to_read:</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code js-file-line">        <span class="pl-k">return</span>(values,none)</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code js-file-line">    <span class="pl-k">for</span> external <span class="pl-kolp">in</span> elements_to_read:</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code js-file-line">        part_id <span class="pl-ko">=</span> id_generator()</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code js-file-line">        filename <span class="pl-ko">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code js-file-line">        <span class="pl-k">if</span> external.tag <span class="pl-ko">==</span> <span class="pl-s1"><span class="pl-pds">&#39;</span>img<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code js-file-line">            filename <span class="pl-ko">=</span> external.get(<span class="pl-s1"><span class="pl-pds">&#39;</span>src<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code js-file-line">            external.set(<span class="pl-s1"><span class="pl-pds">&#39;</span>src<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>name:<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-ko">%</span> part_id)</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code js-file-line">        <span class="pl-k">if</span> external.tag <span class="pl-ko">==</span> <span class="pl-s1"><span class="pl-pds">&#39;</span>object<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code js-file-line">            filename <span class="pl-ko">=</span> external.get(<span class="pl-s1"><span class="pl-pds">&#39;</span>data<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code js-file-line">            external.set(<span class="pl-s1"><span class="pl-pds">&#39;</span>data<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>name:<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-ko">%</span> part_id)</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code js-file-line">        to_attach.append( ( part_id, filename.replace(<span class="pl-s1"><span class="pl-pds">&#39;</span>file://<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>) ) )</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code js-file-line">    files <span class="pl-ko">=</span> collections.OrderedDict()</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code js-file-line">    files[<span class="pl-s1"><span class="pl-pds">&#39;</span>Presentation<span class="pl-pds">&#39;</span></span>] <span class="pl-ko">=</span> (<span class="pl-s1"><span class="pl-pds">&#39;</span>Presentation<span class="pl-pds">&#39;</span></span>,StringIO(<span class="pl-s1"><span class="pl-pds">&#39;</span>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; ?&gt;<span class="pl-pds">&#39;</span></span><span class="pl-ko">+</span>lxml.html.tostring(tree)),<span class="pl-s1"><span class="pl-pds">&#39;</span>application/xhtml+xml<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code js-file-line">    <span class="pl-k">for</span> (part, attachment) <span class="pl-kolp">in</span> to_attach:</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code js-file-line">        (mimetype,encoding) <span class="pl-ko">=</span> mimetypes.guess_type(attachment)</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code js-file-line">        files[part] <span class="pl-ko">=</span> (attachment, <span class="pl-sf">open</span>(attachment, <span class="pl-s1"><span class="pl-pds">&#39;</span>rb<span class="pl-pds">&#39;</span></span>), mimetype)</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code js-file-line">    <span class="pl-k">return</span> (<span class="pl-s1"><span class="pl-pds">&#39;</span>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; ?&gt;<span class="pl-pds">&#39;</span></span><span class="pl-ko">+</span>lxml.html.tostring(tree),files)</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code js-file-line"><span class="pl-s">def</span> <span class="pl-enf">write_page</span>(<span class="pl-vpf">client</span>,<span class="pl-vpf">notebook_name</span>,<span class="pl-vpf">section_name</span>,<span class="pl-vpf">filename</span>):</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code js-file-line">    (html,files) <span class="pl-ko">=</span> read_html(filename)</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code js-file-line">    datas <span class="pl-ko">=</span> client.do_request(<span class="pl-vpf">url</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span>notebooks<span class="pl-pds">&#39;</span></span>, <span class="pl-vpf">query</span><span class="pl-ko">=</span>{<span class="pl-s1"><span class="pl-pds">&#39;</span>filter<span class="pl-pds">&#39;</span></span> : <span class="pl-s1"><span class="pl-pds">&quot;</span>name eq <span class="pl-cce">\&#39;</span><span class="pl-c1">%s</span><span class="pl-cce">\&#39;</span><span class="pl-pds">&quot;</span></span> <span class="pl-ko">%</span> notebook_name, <span class="pl-s1"><span class="pl-pds">&#39;</span>select<span class="pl-pds">&#39;</span></span> : <span class="pl-s1"><span class="pl-pds">&quot;</span>id<span class="pl-pds">&quot;</span></span> })[<span class="pl-s1"><span class="pl-pds">&#39;</span>value<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code js-file-line">    <span class="pl-k">if</span> datas:</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code js-file-line">        notebook_id <span class="pl-ko">=</span> datas[<span class="pl-cn">0</span>][<span class="pl-s1"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code js-file-line">        datas <span class="pl-ko">=</span> client.do_request(<span class="pl-vpf">url</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span>notebooks/<span class="pl-c1">%s</span>/sections<span class="pl-pds">&#39;</span></span> <span class="pl-ko">%</span> notebook_id, <span class="pl-vpf">query</span><span class="pl-ko">=</span>{<span class="pl-s1"><span class="pl-pds">&#39;</span>select<span class="pl-pds">&#39;</span></span> : <span class="pl-s1"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span>} )[<span class="pl-s1"><span class="pl-pds">&#39;</span>value<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code js-file-line">        <span class="pl-k">if</span> datas:</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code js-file-line">            section_id <span class="pl-ko">=</span> datas[<span class="pl-cn">0</span>][<span class="pl-s1"><span class="pl-pds">&#39;</span>id<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code js-file-line">    <span class="pl-k">if</span> notebook_id <span class="pl-kolp">and</span> section_id:</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code js-file-line">        <span class="pl-k">if</span> (files):</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code js-file-line">            <span class="pl-k">print</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>Sending file attachments<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code js-file-line">            datas <span class="pl-ko">=</span> client.do_request(<span class="pl-s1"><span class="pl-pds">&#39;</span>sections/<span class="pl-c1">%s</span>/pages<span class="pl-pds">&#39;</span></span> <span class="pl-ko">%</span> section_id, <span class="pl-vpf">method</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span>post<span class="pl-pds">&#39;</span></span>, <span class="pl-vpf">files</span><span class="pl-ko">=</span>files )</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code js-file-line">            datas <span class="pl-ko">=</span> client.do_request(<span class="pl-s1"><span class="pl-pds">&#39;</span>sections/<span class="pl-c1">%s</span>/pages<span class="pl-pds">&#39;</span></span> <span class="pl-ko">%</span> section_id,<span class="pl-vpf">data</span> <span class="pl-ko">=</span> html, <span class="pl-vpf">method</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span>post<span class="pl-pds">&#39;</span></span>, <span class="pl-vpf">headers</span> <span class="pl-ko">=</span> { <span class="pl-s1"><span class="pl-pds">&#39;</span>Content-Type<span class="pl-pds">&#39;</span></span>: <span class="pl-s1"><span class="pl-pds">&#39;</span>application/xhtml+xml<span class="pl-pds">&#39;</span></span> })</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code js-file-line">        <span class="pl-k">print</span> datas</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code js-file-line"><span class="pl-s">class</span> <span class="pl-entc">OneDrive</span>(<span class="pl-eoi">OneDriveAuth</span>):</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code js-file-line">    api_url_base <span class="pl-ko">=</span> <span class="pl-s1"><span class="pl-pds">&#39;</span>https://www.onenote.com/api/v1.0/<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code js-file-line">    <span class="pl-s">def</span> <span class="pl-enf">_api_url</span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">path</span>, <span class="pl-vpf">query</span><span class="pl-ko">=</span><span class="pl-st">dict</span>(),</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code js-file-line">                 <span class="pl-vpf">pass_access_token</span><span class="pl-ko">=</span><span class="pl-c1">True</span>, <span class="pl-vpf">pass_empty_values</span><span class="pl-ko">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code js-file-line">        query <span class="pl-ko">=</span> query.copy()</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code js-file-line">        <span class="pl-k">if</span> pass_access_token:</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code js-file-line">            query.setdefault(<span class="pl-s1"><span class="pl-pds">&#39;</span>access_token<span class="pl-pds">&#39;</span></span>, <span class="pl-v">self</span>.auth_access_token)</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code js-file-line">        <span class="pl-k">if</span> <span class="pl-kolp">not</span> pass_empty_values:</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code js-file-line">            <span class="pl-k">for</span> k, v <span class="pl-kolp">in</span> query.viewitems():</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code js-file-line">                <span class="pl-k">if</span> <span class="pl-kolp">not</span> v <span class="pl-kolp">and</span> v <span class="pl-ko">!=</span> <span class="pl-cn">0</span>:</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code js-file-line">                    <span class="pl-k">raise</span> AuthenticationError(</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code js-file-line">                        <span class="pl-s1"><span class="pl-pds">&#39;</span>Empty key <span class="pl-c1">{!r}</span> for API call (path: <span class="pl-c1">{}</span>)<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code js-file-line">                        .format(k, path))</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code js-file-line">        <span class="pl-k">return</span> urlparse.urljoin(<span class="pl-v">self</span>.api_url_base,</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code js-file-line">                                <span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-c1">{}</span>?<span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(path, urllib.urlencode(query)))</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code js-file-line">    <span class="pl-s">def</span> <span class="pl-enf">do_request</span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">url</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span>notebooks<span class="pl-pds">&#39;</span></span>, <span class="pl-vpf">query</span><span class="pl-ko">=</span><span class="pl-st">dict</span>(), <span class="pl-vpf">query_filter</span><span class="pl-ko">=</span><span class="pl-c1">True</span>, <span class="pl-vpf">auth_header</span><span class="pl-ko">=</span><span class="pl-c1">True</span>, <span class="pl-vpf">auto_refresh_token</span><span class="pl-ko">=</span><span class="pl-c1">True</span>, **<span class="pl-vpf">request_kwz</span>):</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code js-file-line">        <span class="pl-s1"><span class="pl-pds">&quot;&quot;&quot;</span>Make an arbitrary call to LiveConnect API.</span></td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code js-file-line"><span class="pl-s1">            Shouldn&#39;t be used directly under most circumstances.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code js-file-line">        <span class="pl-k">if</span> query_filter:</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code js-file-line">            query <span class="pl-ko">=</span> <span class="pl-st">dict</span>((k, v) <span class="pl-k">for</span> k, v <span class="pl-kolp">in</span></td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code js-file-line">                         query.viewitems() <span class="pl-k">if</span> v <span class="pl-kolp">is</span> <span class="pl-kolp">not</span> <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code js-file-line">        <span class="pl-k">if</span> auth_header:</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code js-file-line">            request_kwz.setdefault(<span class="pl-s1"><span class="pl-pds">&#39;</span>headers<span class="pl-pds">&#39;</span></span>, <span class="pl-st">dict</span>())[<span class="pl-s1"><span class="pl-pds">&#39;</span>Authorization<span class="pl-pds">&#39;</span></span>] <span class="pl-ko">=</span> (</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code js-file-line">                <span class="pl-s1"><span class="pl-pds">&#39;</span>Bearer <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-v">self</span>.auth_access_token))</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code js-file-line">        kwz <span class="pl-ko">=</span> request_kwz.copy()</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code js-file-line">        kwz.setdefault(<span class="pl-s1"><span class="pl-pds">&#39;</span>raise_for<span class="pl-pds">&#39;</span></span>, <span class="pl-st">dict</span>())[<span class="pl-cn">401</span>] <span class="pl-ko">=</span> AuthenticationError</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code js-file-line">        api_url <span class="pl-ko">=</span> ft.partial(<span class="pl-v">self</span>._api_url,</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code js-file-line">                             url, query, <span class="pl-vpf">pass_access_token</span><span class="pl-ko">=</span><span class="pl-kolp">not</span> auth_header)</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code js-file-line">            <span class="pl-k">return</span> <span class="pl-v">self</span>.request(api_url(), <span class="pl-ko">**</span>kwz)</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code js-file-line">        <span class="pl-k">except</span> AuthenticationError:</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code js-file-line">            <span class="pl-k">if</span> <span class="pl-kolp">not</span> auto_refresh_token:</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code js-file-line">                <span class="pl-k">raise</span></td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code js-file-line">            <span class="pl-v">self</span>.auth_get_token()</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code js-file-line">            <span class="pl-k">if</span> auth_header:  <span class="pl-c"><span class="pl-pdc">#</span> update auth header with a new token</span></td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code js-file-line">                request_kwz[<span class="pl-s1"><span class="pl-pds">&#39;</span>headers<span class="pl-pds">&#39;</span></span>][<span class="pl-s1"><span class="pl-pds">&#39;</span>Authorization<span class="pl-pds">&#39;</span></span>] \</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code js-file-line">                    <span class="pl-ko">=</span> <span class="pl-s1"><span class="pl-pds">&#39;</span>Bearer <span class="pl-c1">{}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-v">self</span>.auth_access_token)</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code js-file-line">            <span class="pl-k">return</span> <span class="pl-v">self</span>.request(api_url(), <span class="pl-ko">**</span>request_kwz)</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code js-file-line"><span class="pl-s">def</span> <span class="pl-enf">get_client</span>(<span class="pl-vpf">force</span><span class="pl-ko">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code js-file-line">    <span class="pl-s">global</span> auth_code</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code js-file-line">    <span class="pl-s">global</span> KEEP_RUNNING</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code js-file-line">    config_file <span class="pl-ko">=</span> <span class="pl-s1"><span class="pl-pds">&#39;</span>onenote.cfg<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code js-file-line">    config <span class="pl-ko">=</span> ConfigParser.SafeConfigParser({</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code js-file-line">                <span class="pl-s1"><span class="pl-pds">&#39;</span>client_id<span class="pl-pds">&#39;</span></span>:<span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code js-file-line">                <span class="pl-s1"><span class="pl-pds">&#39;</span>client_secret<span class="pl-pds">&#39;</span></span>:<span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code js-file-line">                })</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code js-file-line">    config.read( [ config_file, os.path.expanduser(<span class="pl-s1"><span class="pl-pds">&#39;</span>~/.onenote.cfg<span class="pl-pds">&#39;</span></span>) ])</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code js-file-line">    <span class="pl-k">if</span> <span class="pl-kolp">not</span> config.has_section(<span class="pl-s1"><span class="pl-pds">&#39;</span>onenote<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code js-file-line">        config.add_section(<span class="pl-s1"><span class="pl-pds">&#39;</span>onenote<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code js-file-line">    client_id <span class="pl-ko">=</span> config.get(<span class="pl-s1"><span class="pl-pds">&#39;</span>onenote<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>client_id<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code js-file-line">    client_secret <span class="pl-ko">=</span> config.get(<span class="pl-s1"><span class="pl-pds">&#39;</span>onenote<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>client_secret<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code js-file-line">    client <span class="pl-ko">=</span> OneDrive(<span class="pl-vpf">client_id</span><span class="pl-ko">=</span>client_id,<span class="pl-vpf">client_secret</span><span class="pl-ko">=</span>client_secret,<span class="pl-vpf">auth_redirect_uri</span><span class="pl-ko">=</span><span class="pl-s1"><span class="pl-pds">&#39;</span>http://ronenote.localtest.me:8000<span class="pl-pds">&#39;</span></span>, <span class="pl-vpf">auth_scope</span><span class="pl-ko">=</span>(<span class="pl-s1"><span class="pl-pds">&#39;</span>office.onenote_create<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>office.onenote_update<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>wl.offline_access<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code js-file-line">    refresh_token <span class="pl-ko">=</span> keyring.get_password(<span class="pl-s1"><span class="pl-pds">&#39;</span>onenote<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>refresh_token<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code js-file-line">    <span class="pl-k">if</span> force <span class="pl-kolp">or</span> refresh_token <span class="pl-kolp">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code js-file-line">        <span class="pl-k">print</span> <span class="pl-ko">&gt;&gt;</span> sys.stderr, <span class="pl-s1"><span class="pl-pds">&quot;</span>Performing a new login<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code js-file-line">        <span class="pl-k">print</span> client.auth_user_get_url()</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code js-file-line">        server_class <span class="pl-ko">=</span> BaseHTTPServer.HTTPServer</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code js-file-line">        httpd <span class="pl-ko">=</span> server_class((<span class="pl-s1"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>, <span class="pl-cn">8000</span>), AuthHandler)</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code js-file-line">        KEEP_RUNNING <span class="pl-ko">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code js-file-line">        <span class="pl-s">def</span> <span class="pl-enf">keep_running</span>():</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code js-file-line">            <span class="pl-s">global</span> KEEP_RUNNING</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code js-file-line">            <span class="pl-k">return</span> KEEP_RUNNING</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code js-file-line">            <span class="pl-k">while</span> keep_running():</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code js-file-line">                httpd.handle_request()</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code js-file-line">        <span class="pl-k">except</span> <span class="pl-st">KeyboardInterrupt</span>:</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code js-file-line">            <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code js-file-line">        httpd.server_close()</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code js-file-line">        client.auth_user_process_url(auth_code)</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code js-file-line">        client.auth_refresh_token <span class="pl-ko">=</span> refresh_token</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code js-file-line">        client.auth_get_token()</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code js-file-line">    <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code js-file-line">        <span class="pl-k">return</span> get_client(<span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code js-file-line">    keyring.set_password(<span class="pl-s1"><span class="pl-pds">&#39;</span>onenote<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>refresh_token<span class="pl-pds">&#39;</span></span>, client.auth_refresh_token)</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code js-file-line">    <span class="pl-c"><span class="pl-pdc">#</span> Spit back a username/client combo</span></td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code js-file-line">    <span class="pl-k">return</span> client</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code js-file-line"><span class="pl-k">if</span> __name__ <span class="pl-ko">==</span> <span class="pl-s1"><span class="pl-pds">&quot;</span>__main__<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code js-file-line">    main()</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code js-file-line">
</td>
      </tr>
</table>

  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="https://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.08458s from github-fe116-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents js-suggester-field" placeholder=""></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-2d727fed4d969b14b28165c75ad12d7dddd56c0198fa70cedc3fdad7ac395b2c.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-cefdded3b042fd290e36fc3bec2c1744521e97ee583e06c43e76cc545f24a273.js" type="text/javascript"></script>
      
      
  </body>
</html>

